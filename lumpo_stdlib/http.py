# basic http server and router for lumpo

import socket
import threading
import urllib.parse
import re

_status_codes = {
    200: "OK",
    201: "Created",
    204: "No Content",
    301: "Moved Permanently",
    302: "Found",
    304: "Not Modified",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    409: "Conflict",
    413: "Payload Too Large",
    429: "Too Many Requests",
    500: "Internal Server Error",
    502: "Bad Gateway",
    503: "Service Unavailable",
}


def status_text(code):
    return _status_codes.get(code, "Unknown")


class _Router:
    def __init__(self):
        self.routes = []  # list of (method, pattern, param_names, regex, handler)
        self.middlewares = []

    def use(self, mw):
        """register a middleware function: mw(req) -> response or None"""
        self.middlewares.append(mw)

    def _compile_route(self, path):
        # Convert /users/:id to regex ^/users/(?P<id>[^/]+)$
        param_names = re.findall(r':([a-zA-Z_]\w*)', path)
        regex_str = '^' + re.sub(r':([a-zA-Z_]\w*)', r'(?P<\1>[^/]+)', path) + '$'
        return param_names, re.compile(regex_str)

    def _add(self, method, path, fn):
        param_names, regex = self._compile_route(path)
        self.routes.append((method.upper(), path, param_names, regex, fn))

    def get(self, path, fn):
        self._add('GET', path, fn)

    def post(self, path, fn):
        self._add('POST', path, fn)

    def put(self, path, fn):
        self._add('PUT', path, fn)

    def delete(self, path, fn):
        self._add('DELETE', path, fn)

    def patch(self, path, fn):
        self._add('PATCH', path, fn)

    def handle(self, req):
        if not isinstance(req, dict):
            return 500, 'text/plain', 'invalid request object'

        # Execute middlewares
        for mw in self.middlewares:
            try:
                res = mw(req)
                if res is not None:
                    return res
            except Exception as e:
                return 500, 'text/plain', f'middleware error: {e}'

        method = req.get('method', 'GET').upper()
        path = req.get('path', '/')

        # Match routes
        for r_method, r_path, param_names, regex, handler in self.routes:
            if r_method == method or r_method == '*':
                match = regex.match(path)
                if match:
                    # populate params
                    req['params'] = match.groupdict()
                    try:
                        return handler(req)
                    except Exception as e:
                        return 500, 'text/plain', f'handler error: {e}'

        return 404, 'text/plain', 'not found'


router = _Router()


def listen(port, handler):
    """start a simple http server on *port* using *handler*."""

    def _handle(conn):
        try:
            data = conn.recv(4096).decode('utf-8', errors='replace')
            if not data:
                return
            lines = data.splitlines()
            if not lines:
                return
            parts = lines[0].split()
            if len(parts) < 2:
                return
            method, path = parts[0], parts[1]
            req_parts = urllib.parse.urlparse(path)
            query = urllib.parse.parse_qs(req_parts.query)

            headers = {}
            body_start = 0
            for i, line in enumerate(lines[1:], 1):
                if not line.strip():
                    body_start = i + 1
                    break
                if ':' in line:
                    k, v = line.split(':', 1)
                    headers[k.strip().lower()] = v.strip()

            body = '\n'.join(lines[body_start:]) if body_start < len(lines) else ''

            request = {
                'method': method,
                'path': req_parts.path,
                'query': query,
                'params': {},
                'headers': headers,
                'body': body,
            }
            try:
                result = handler(request)
            except Exception as e:
                result = [500, 'text/plain', str(e)]

            if isinstance(result, (list, tuple)):
                status = result[0]
                ctype = result[1] if len(result) > 1 else 'text/plain'
                resp_body = result[2] if len(result) > 2 else ''
            else:
                status, ctype, resp_body = 200, 'text/plain', str(result)

            status_line = f"HTTP/1.1 {status} {status_text(status)}"
            body_bytes = str(resp_body).encode('utf-8')
            resp = (
                f"{status_line}\r\n"
                f"Content-Type: {ctype}\r\n"
                f"Content-Length: {len(body_bytes)}\r\n"
                f"Connection: close\r\n\r\n"
            ).encode('utf-8') + body_bytes
            conn.sendall(resp)
        finally:
            conn.close()

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('0.0.0.0', port))
    srv.listen(5)
    print(f"lumpo http listening on :{port}")
    while True:
        conn, _ = srv.accept()
        threading.Thread(target=_handle, args=(conn,)).start()
