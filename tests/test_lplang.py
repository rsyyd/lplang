# tests/test_lplang.py
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


class TestLPLangCore(unittest.TestCase):
    def test_variable_binding(self):
        res = run_src('let x = 10\nprint x\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "10")

    def test_string_interpolation(self):
        res = run_src('let name = "LPLang"\nprint "hello ${name}"\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "hello LPLang")

    def test_function_definition(self):
        res = run_src('fn add(a, b) { return a + b }\nprint add(3, 4)\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "7")

    def test_function_rejects_wrong_argument_count(self):
        too_few = run_src('fn add(a, b) { return a + b }\nprint add(3)\n')
        self.assertNotEqual(too_few.returncode, 0)
        self.assertIn("expected 2 arguments, got 1", too_few.stderr)

        too_many = run_src('fn add(a, b) { return a + b }\nprint add(3, 4, 5)\n')
        self.assertNotEqual(too_many.returncode, 0)
        self.assertIn("expected 2 arguments, got 3", too_many.stderr)

    def test_component_rejects_wrong_argument_count(self):
        too_few = run_src('component Card(name) { print name }\nCard()\n')
        self.assertNotEqual(too_few.returncode, 0)
        self.assertIn("expected 1 arguments, got 0", too_few.stderr)

        too_many = run_src('component Card(name) { print name }\nCard("x", "y")\n')
        self.assertNotEqual(too_many.returncode, 0)
        self.assertIn("expected 1 arguments, got 2", too_many.stderr)

    def test_array_literal(self):
        res = run_src('let arr = [1, 2, 3]\nprint len(arr)\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "3")

    def test_map_literal(self):
        res = run_src('let m = {status: "ok"}\nprint m["status"]\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "ok")

    def test_map_dot_access(self):
        res = run_src('let m = {a: 1, b: 2}\nprint m.a\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "1")


if __name__ == "__main__":
    unittest.main()