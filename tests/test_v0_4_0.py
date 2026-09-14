"""v0.4.0 language-completeness tests: switch, compound assign, break/continue,
block comments, null-coalescing, ternary, new string methods, range step.
Written BEFORE implementation (TDD)."""
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


class TestSwitch(unittest.TestCase):
    def test_switch_basic(self):
        res = run_lp('''
let x = 2
switch x {
    case 1 { print "one" }
    case 2 { print "two" }
    case 3 { print "three" }
    default { print "other" }
}
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("two", res.stdout)
        self.assertNotIn("one", res.stdout)

    def test_switch_default(self):
        res = run_lp('''
switch 99 {
    case 1 { print "one" }
    default { print "fallback" }
}
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("fallback", res.stdout)

    def test_switch_string(self):
        res = run_lp('''
let k = "b"
switch k {
    case "a" { print "alpha" }
    case "b" { print "beta" }
}
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("beta", res.stdout)


class TestCompoundAssign(unittest.TestCase):
    def test_compound_ops(self):
        res = run_lp('''
let x = 10
x += 5
print x
x -= 3
print x
x *= 4
print x
x /= 2
print x
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        lines = [l.strip() for l in res.stdout.strip().split("\n")]
        self.assertEqual(lines, ["15", "12", "48", "24"])


class TestBreakContinue(unittest.TestCase):
    def test_break(self):
        res = run_lp('''
let i = 0
while true {
    i += 1
    if i == 3 { break }
}
print i
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("3", res.stdout)

    def test_continue(self):
        res = run_lp('''
let total = 0
for i in range(1, 6) {
    if i == 3 { continue }
    total += i
}
print total
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("12", res.stdout)  # 1+2+4+5


class TestBlockComments(unittest.TestCase):
    def test_block_comment(self):
        res = run_lp('''
/* comment
   multi line */
let x = 42
print x
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("42", res.stdout)

    def test_block_comment_inline(self):
        res = run_lp('let y = 7 /* oke */ + 3\nprint y\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("10", res.stdout)


class TestNullCoalescing(unittest.TestCase):
    def test_null_coalesce(self):
        res = run_lp('''
let a = null
print a ?? "default"
let b = "value"
print b ?? "default"
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        lines = [l.strip() for l in res.stdout.strip().split("\n")]
        self.assertEqual(lines, ["default", "value"])


class TestTernary(unittest.TestCase):
    def test_ternary(self):
        res = run_lp('''
let age = 17
let status = age >= 18 ? "adult" : "minor"
print status
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("minor", res.stdout)


class TestStringMethods(unittest.TestCase):
    def test_new_string_methods(self):
        res = run_lp('''
let s = "lumpo"
print starts_with(s, "lum")
print ends_with(s, "po")
print repeat("ab", 3)
print pad_left("7", 3, "0")
print index_of("hello", "ll")
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        lines = [l.strip() for l in res.stdout.strip().split("\n")]
        self.assertEqual(lines, ["True", "True", "ababab", "007", "2"])


class TestRangeStep(unittest.TestCase):
    def test_range_step(self):
        res = run_lp('''
let out = []
for i in range(0, 10, 2) {
    push(out, i)
}
print join(out, ",")
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("0,2,4,6,8", res.stdout)


if __name__ == "__main__":
    unittest.main()
