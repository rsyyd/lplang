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

class TestV050Features(unittest.TestCase):

    def test_defer_statement(self):
        src = """
        let logs = []
        fn test_defer() {
            append(logs, "start")
            defer append(logs, "cleanup 1")
            defer append(logs, "cleanup 2")
            append(logs, "end")
        }
        test_defer()
        print join(logs, ", ")
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("start, end, cleanup 2, cleanup 1", res.stdout)

    def test_pipe_operator(self):
        src = """
        fn add(a, b) { return a + b }
        fn double(x) { return x * 2 }

        let res = 5 |> double() |> add(10)
        print res
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("20", res.stdout)

    def test_arrow_function(self):
        src = """
        let add = (a, b) => a + b
        let double = x => x * 2
        print double(add(3, 4))
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("14", res.stdout)

    def test_optional_chaining(self):
        src = """
        let user = {"profile": {"name": "Renz"}}
        let null_user = null

        print user?.profile?.name
        print null_user?.profile?.name
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("Renz", res.stdout)
        self.assertIn("null", res.stdout)

    def test_destructuring_assignment(self):
        src = """
        let [a, b] = [10, 20]
        let {x, y} = {"x": 100, "y": 200}
        print "${a}-${b}-${x}-${y}"
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("10-20-100-200", res.stdout)

if __name__ == '__main__':
    unittest.main()
