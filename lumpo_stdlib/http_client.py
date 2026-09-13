# lumpo_stdlib/http_client.py
"""simple HTTP client for lumpo"""
import urllib.request
import urllib.error
import json as _json

def get(url, headers=None):
    """GET request, returns dict with status, headers, body"""
    req = urllib.request.Request(url, method='GET')
    if headers:
        for k, v in headers.items():
            req.add_header(k, str(v))
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode('utf-8')
            return {
                'status': resp.status,
                'headers': dict(resp.headers),
                'body': body,
            }
    except urllib.error.HTTPError as e:
        return {
            'status': e.code,
            'headers': dict(e.headers),
            'body': e.read().decode('utf-8'),
        }
    except urllib.error.URLError as e:
        return {
            'status': 0,
            'headers': {},
            'body': str(e),
        }

def post(url, data=None, headers=None):
    """POST request"""
    body = data.encode('utf-8') if isinstance(data, str) else data
    req = urllib.request.Request(url, data=body, method='POST')
    if headers:
        for k, v in headers.items():
            req.add_header(k, str(v))
    if body and 'Content-Type' not in str(headers):
        req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return {
                'status': resp.status,
                'headers': dict(resp.headers),
                'body': resp.read().decode('utf-8'),
            }
    except urllib.error.HTTPError as e:
        return {
            'status': e.code,
            'headers': dict(e.headers),
            'body': e.read().decode('utf-8'),
        }
    except urllib.error.URLError as e:
        return {
            'status': 0,
            'headers': {},
            'body': str(e),
        }

def request(method, url, data=None, headers=None):
    """generic HTTP request"""
    body = data.encode('utf-8') if isinstance(data, str) else data
    req = urllib.request.Request(url, data=body, method=method.upper())
    if headers:
        for k, v in headers.items():
            req.add_header(k, str(v))
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return {
                'status': resp.status,
                'headers': dict(resp.headers),
                'body': resp.read().decode('utf-8'),
            }
    except urllib.error.HTTPError as e:
        return {
            'status': e.code,
            'headers': dict(e.headers),
            'body': e.read().decode('utf-8'),
        }
    except urllib.error.URLError as e:
        return {
            'status': 0,
            'headers': {},
            'body': str(e),
        }