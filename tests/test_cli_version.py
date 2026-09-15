import unittest
import subprocess
import os

LUMPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "lumpo")

class TestCliVersion(unittest.TestCase):

    def test_version_flag_prints_version(self):
        res = subprocess.run([LUMPO, "--version"], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn("lumpo v", res.stdout)
        self.assertRegex(res.stdout.strip(), r"^lumpo v\d+\.\d+\.\d+$")

    def test_help_flag_prints_usage_and_succeeds(self):
        res = subprocess.run([LUMPO, "--help"], capture_output=True, text=True)
        self.assertEqual(res.returncode, 0)
        self.assertIn("usage: lumpo <command> [args]", res.stdout)
        self.assertIn("--version", res.stdout)

    def test_repl_banner_uses_version(self):
        res = subprocess.run([LUMPO, "repl"], input="exit\n", capture_output=True, text=True, timeout=10)
        self.assertIn("REPL", res.stdout)
        self.assertRegex(res.stdout, r"lumpo v\d+\.\d+\.\d+ REPL")

    def test_symlinked_cli_finds_standard_library(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as temp_dir:
            cli = Path(temp_dir) / "lumpo"
            cli.symlink_to(LUMPO)
            source = Path(temp_dir) / "program.lp"
            source.write_text('import "math"\nprint math.sqrt(16)\n')
            res = subprocess.run([cli, "run", source], capture_output=True, text=True)

        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "4.0")

if __name__ == '__main__':
    unittest.main()