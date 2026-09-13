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
        return subprocess.run([LUMPO, "run", path], capture_output=True, text=True, timeout=timeout)
    finally:
        os.unlink(path)


class TestErrorReporting(unittest.TestCase):

    def test_index_out_of_range_has_line_number(self):
        res = run_lp("let nums = [1, 2, 3]\nprint nums[9]\n")
        self.assertNotEqual(res.returncode, 0)
        self.assertIn("(line 2)", res.stderr)
        self.assertIn("list index out of range", res.stderr)

    def test_keyerror_has_line_number(self):
        res = run_lp("let m = { 'a': 1 }\nprint m['missing']\n")
        self.assertNotEqual(res.returncode, 0)
        self.assertIn("(line 2)", res.stderr)

    def test_undefined_variable_has_line_number(self):
        res = run_lp("print unknown_var\n")
        self.assertNotEqual(res.returncode, 0)
        self.assertIn("(line 1)", res.stderr)
        self.assertIn("undefined variable 'unknown_var'", res.stderr)

    def test_caught_error_has_clean_message(self):
        res = run_lp(
            "let nums = [1, 2, 3]\n"
            "try {\n"
            "    print nums[9]\n"
            "} catch e {\n"
            "    print \"caught: ${e}\"\n"
            "}\n"
        )
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "caught: list index out of range")
        # no internal "(line N)" noise leaking into user-caught value
        self.assertNotIn("(line", res.stdout)

    def test_struct_error_has_line_of_expression(self):
        res = run_lp(
            "struct Person { name }\n"
            "let p = Person { name: 'L' }\n"
            "print p.missing\n"
        )
        self.assertNotEqual(res.returncode, 0)
        self.assertIn("(line 3)", res.stderr)
        self.assertIn("no attribute 'missing'", res.stderr)


if __name__ == '__main__':
    unittest.main()