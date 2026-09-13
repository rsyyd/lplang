# tests/test_lumpo_v2.py
import unittest
import subprocess
import tempfile
import os

LUMPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lumpo")


def run_src(src):
    fd, path = tempfile.mkstemp(suffix=".lp")
    os.close(fd)
    with open(path, "w") as f:
        f.write(src)
    try:
        res = subprocess.run([LUMPO, "run", path],
                              capture_output=True, text=True, timeout=10)
        return res
    finally:
        os.unlink(path)


class TestLumpoV2(unittest.TestCase):
    def test_full_program(self):
        res = run_src('let x = 10\nlet y = 20\nlet z = x + y * 2\nprint z\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "50")

    def test_arithmetic_operators(self):
        for code, exp in [("let a = 10 + 5\nprint a\n", "15"),
                         ("let b = 20 - 8\nprint b\n", "12"),
                         ("let c = 3 * 4\nprint c\n", "12"),
                         ("let d = 15 / 3\nprint d\n", "5")]:
            res = run_src(code)
            self.assertEqual(res.returncode, 0, f"stderr: {res.stderr}")
            self.assertEqual(res.stdout.strip(), exp)

    def test_comparison_operators(self):
        res = run_src('let a = 5\nprint a > 3\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("True", res.stdout)

    def test_boolean_operators(self):
        res = run_src('print true and false\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("False", res.stdout)


if __name__ == "__main__":
    unittest.main()