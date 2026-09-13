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

    def test_repl_banner_uses_version(self):
        res = subprocess.run([LUMPO, "repl"], input="exit\n", capture_output=True, text=True, timeout=10)
        self.assertIn("REPL", res.stdout)
        self.assertRegex(res.stdout, r"lumpo v\d+\.\d+\.\d+ REPL")

if __name__ == '__main__':
    unittest.main()