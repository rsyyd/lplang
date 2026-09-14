"""v0.3.0 language-core tests: try/catch/throw, local imports, math/time modules,
functional builtins. Written BEFORE implementation (TDD)."""
import unittest
import subprocess
import tempfile
import os

LUMPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lumpo")


def run_lp(src, timeout=10):
    fd, path = tempfile.mkstemp(suffix=".lp")
    os.close(fd)
    with open(path, "w") as f:
        f.write(src)
    try:
        return subprocess.run([LUMPO, "run", path],
                              capture_output=True, text=True, timeout=timeout)
    finally:
        os.unlink(path)


class TestTryCatchThrow(unittest.TestCase):
    def test_catch_thrown_value(self):
        res = run_lp('''
fn risky() {
    throw "boom"
}
try {
    risky()
} catch e {
    print "caught: ${e}"
}
print "after"
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("caught: boom", res.stdout)
        self.assertIn("after", res.stdout)

    def test_catch_runtime_error(self):
        res = run_lp('''
try {
    let x = undefined_var + 1
} catch e {
    print "err happened"
}
print "survived"
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("err happened", res.stdout)
        self.assertIn("survived", res.stdout)

    def test_uncaught_throw_fails(self):
        res = run_lp('throw "fatal"\n')
        self.assertNotEqual(res.returncode, 0)

    def test_try_no_error_skips_catch(self):
        res = run_lp('''
try {
    print "body"
} catch e {
    print "should-not-print"
}
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("body", res.stdout)
        self.assertNotIn("should-not-print", res.stdout)


class TestLocalImports(unittest.TestCase):
    def test_import_local_file(self):
        d = tempfile.mkdtemp()
        lib = os.path.join(d, "helpers.lp")
        main = os.path.join(d, "main.lp")
        with open(lib, "w") as f:
            f.write('fn double(n) {\n    return n * 2\n}\nlet VERSION = "1.2"\n')
        with open(main, "w") as f:
            f.write('import "./helpers.lp"\nprint double(21)\nprint helpers.VERSION\n')
        res = subprocess.run([LUMPO, "run", main],
                             capture_output=True, text=True, timeout=10)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("42", res.stdout)
        self.assertIn("1.2", res.stdout)


class TestMathTimeModules(unittest.TestCase):
    def test_math_module(self):
        res = run_lp('''
import "math"
print math.sqrt(16)
print math.pow(2, 10)
print math.floor(3.9)
print math.ceil(3.1)
print math.round(3.5)
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        lines = [l.strip() for l in res.stdout.strip().split("\n")]
        self.assertEqual(lines[0], "4.0")
        self.assertEqual(lines[1], "1024")
        self.assertEqual(lines[2], "3")
        self.assertEqual(lines[3], "4")
        self.assertEqual(lines[4], "4")

    def test_time_module(self):
        res = run_lp('''
import "time"
let t1 = time.now()
time.sleep(0.05)
let t2 = time.now()
assert(t2 > t1, "time should advance")
print "time ok"
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("time ok", res.stdout)


class TestFunctionalBuiltins(unittest.TestCase):
    def test_map_filter_reduce(self):
        res = run_lp('''
let nums = [1, 2, 3, 4, 5]
let doubled = map(nums, fn(n) { return n * 2 })
print doubled[0]
print doubled[4]
let evens = filter(nums, fn(n) { return n % 2 == 0 })
print len(evens)
let total = reduce(nums, fn(acc, n) { return acc + n }, 0)
print total
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        lines = [l.strip() for l in res.stdout.strip().split("\n")]
        self.assertEqual(lines[0], "2")
        self.assertEqual(lines[1], "10")
        self.assertEqual(lines[2], "2")
        self.assertEqual(lines[3], "15")

    def test_find_any_all(self):
        res = run_lp('''
let nums = [3, 7, 11]
print find(nums, fn(n) { return n > 5 })
print any(nums, fn(n) { return n > 10 })
print any(nums, fn(n) { return n > 100 })
print all(nums, fn(n) { return n > 0 })
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        lines = [l.strip() for l in res.stdout.strip().split("\n")]
        self.assertEqual(lines[0], "7")
        self.assertEqual(lines[1], "True")
        self.assertEqual(lines[2], "False")
        self.assertEqual(lines[3], "True")


class TestConst(unittest.TestCase):
    def test_const_defined_and_used(self):
        res = run_lp('''
const PI = 3.14
print PI
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("3.14", res.stdout)

    def test_const_cannot_reassign(self):
        res = run_lp('''
const MAX = 100
MAX = 200
''')
        self.assertNotEqual(res.returncode, 0)
        self.assertIn("reassign", res.stderr)

    def test_let_still_reassignable(self):
        res = run_lp('''
let x = 1
x = 2
print x
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("2", res.stdout)


if __name__ == "__main__":
    unittest.main()
