import unittest
import subprocess
import tempfile
import os
from pathlib import Path

LUMPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lumpo")


def run_cmd(args, timeout=10):
    return subprocess.run([LUMPO] + args, capture_output=True, text=True, timeout=timeout)


def run_lp(src, timeout=10):
    fd, path = tempfile.mkstemp(suffix=".lp")
    os.close(fd)
    with open(path, "w") as f:
        f.write(src)
    try:
        return run_cmd(["run", path], timeout=timeout)
    finally:
        os.unlink(path)


class TestV110Features(unittest.TestCase):
    def test_assert_builtin_success_and_failure(self):
            # assert(true) should pass
            res_ok = run_lp('assert(1 + 1 == 2, "math works")\nprint "ok"\n')
            self.assertEqual(res_ok.returncode, 0, res_ok.stderr)
            self.assertIn("ok", res_ok.stdout)

            # assert(false) should fail with clear message
            res_fail = run_lp('assert(1 + 1 == 3, "math failed")\n')
            self.assertNotEqual(res_fail.returncode, 0)
            output = res_fail.stderr + res_fail.stdout
            self.assertIn("math failed", output)

    def test_http_dynamic_params_and_methods(self):
        code = '''
import "http"
import "json"

fn get_user(req) {
    let uid = req.params.id
    return [200, "application/json", json.stringify({user_id: uid})]
}

router.get("/users/:id", get_user)

let req = {method: "GET", path: "/users/42", query: {}, headers: {}}
let resp = router.handle(req)
print resp[0]
print resp[2]
'''
        res = run_lp(code)
        self.assertEqual(res.returncode, 0, res.stderr)
        lines = [l.strip() for l in res.stdout.strip().split("\n") if l.strip()]
        self.assertEqual(lines[0], "200")
        self.assertIn('{"user_id": "42"}', lines[1])

    def test_http_middleware_support(self):
        code = '''
import "http"

fn mw_auth(req) {
    if req.headers.get("x-token", "") != "secret" {
        return [401, "text/plain", "unauthorized"]
    }
    return none
}

router.use(mw_auth)

fn secret_area(req) {
    return [200, "text/plain", "top-secret"]
}

router.get("/secret", secret_area)

# Test without header
let req1 = {method: "GET", path: "/secret", query: {}, headers: {}}
let resp1 = router.handle(req1)
print resp1[0]

# Test with header
let req2 = {method: "GET", path: "/secret", query: {}, headers: {"x-token": "secret"}}
let resp2 = router.handle(req2)
print resp2[0]
print resp2[2]
'''
        res = run_lp(code)
        self.assertEqual(res.returncode, 0, res.stderr)
        lines = [l.strip() for l in res.stdout.strip().split("\n") if l.strip()]
        self.assertEqual(lines[0], "401")
        self.assertEqual(lines[1], "200")
        self.assertEqual(lines[2], "top-secret")

    def test_lumpo_fmt(self):
        unformatted = 'let    x=   10+ 5\nfn foo(a,b){\nreturn a*b\n}\n'
        fd, path = tempfile.mkstemp(suffix=".lp")
        os.close(fd)
        with open(path, "w") as f:
            f.write(unformatted)
        try:
            res = run_cmd(["fmt", path])
            self.assertEqual(res.returncode, 0, res.stderr)
            formatted = Path(path).read_text()
            self.assertIn("let x = 10 + 5", formatted)
            self.assertIn("fn foo(a, b) {", formatted)
            self.assertIn("    return a * b", formatted)
        finally:
            os.unlink(path)

    def test_lumpo_test_command(self):
        # Create a temp test file
        fd, path = tempfile.mkstemp(suffix="_test.lp")
        os.close(fd)
        test_src = '''
fn test_addition() {
    assert(2 + 2 == 4, "2+2 should be 4")
}

fn test_strings() {
    assert("hello" + " " + "world" == "hello world", "string concat")
}

test_addition()
test_strings()
print "all tests passed!"
'''
        with open(path, "w") as f:
            f.write(test_src)
        try:
            res = run_cmd(["test", path])
            self.assertEqual(res.returncode, 0, res.stderr)
            self.assertIn("PASS", res.stdout)
        finally:
            os.unlink(path)

    def test_humanized_error_display(self):
        bad_code = 'let a = 1\nlet b = a + undefined_variable\n'
        res = run_lp(bad_code)
        self.assertNotEqual(res.returncode, 0)
        output = res.stderr + res.stdout
        # should show line number and context snippet
        self.assertIn("line 2", output.lower())
        self.assertIn("undefined_variable", output)


if __name__ == "__main__":
    unittest.main()
