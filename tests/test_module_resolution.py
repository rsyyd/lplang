import unittest
import subprocess
import tempfile
import os
from pathlib import Path

LUMPO = str(Path(__file__).resolve().parent.parent / "lumpo")


def run_in(dirpath, src, timeout=15):
    """write src as main.lp inside dirpath and run it, returning CompletedProcess."""
    main = Path(dirpath) / "main.lp"
    main.write_text(src)
    return subprocess.run([LUMPO, "run", str(main)], capture_output=True, text=True, timeout=timeout)


class TestModuleResolution(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.mkdtemp(prefix="lumpo_mod_")

    def _make_lib(self):
        lib = Path(self._tmp) / "lib"
        lib.mkdir(exist_ok=True)
        (lib / "util.lp").write_text(
            "let version = '1.0.0'\n"
            "fn greeting(name) { return 'hello ' + name }\n"
        )
        return lib

    def test_import_with_explicit_dot_lp(self):
        self._make_lib()
        res = run_in(self._tmp, 'import "./lib/util.lp"\nprint greeting("L")\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "hello L")

    def test_import_without_extension(self):
        self._make_lib()
        res = run_in(self._tmp, 'import "./lib/util"\nprint greeting("L")\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "hello L")

    def test_import_relative_to_cwd(self):
        self._make_lib()
        res = run_in(self._tmp, 'import "lib/util.lp"\nprint greeting("L")\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "hello L")

    def test_stdio_import_uses_stdlib(self):
        res = run_in(self._tmp, 'import "math"\nprint sqrt(16)\n')
        self.assertEqual(res.returncode, 0, res.stderr)
        # sqrt returns float (4.0) - accept either rendering of the value
        self.assertEqual(res.stdout.strip(), "4.0")

    def test_missing_module_errors(self):
        res = run_in(self._tmp, 'import "./nope.lp"\n')
        self.assertNotEqual(res.returncode, 0)
        self.assertIn("not found", res.stderr)


if __name__ == '__main__':
    unittest.main()