"""Tests for new standard library modules: os and struct."""
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


class TestOsModule(unittest.TestCase):
    def test_os_paths(self):
        res = run_lp('''
import "os"
let p = os.path_join("a", "b", "c.txt")
print os.path_ext(p)
print os.path_stem(p)
print len(os.cwd()) > 0
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        lines = [l.strip() for l in res.stdout.strip().split("\n")]
        self.assertEqual(lines[0], ".txt")
        self.assertEqual(lines[1], "c")
        self.assertEqual(lines[2], "True")


class TestStructModule(unittest.TestCase):
    def test_pack_unpack(self):
        res = run_lp('''
import "struct"
let b = struct.pack_int(1337, 4, "big", true)
let val = struct.unpack_int(b, "big", true)
print val

let h = struct.bytes_to_hex([255, 0, 16])
print h
let dec = struct.hex_to_bytes("ff0010")
print dec[0]
print dec[2]
''')
        self.assertEqual(res.returncode, 0, res.stderr)
        lines = [l.strip() for l in res.stdout.strip().split("\n")]
        self.assertEqual(lines[0], "1337")
        self.assertEqual(lines[1], "ff0010")
        self.assertEqual(lines[2], "255")
        self.assertEqual(lines[3], "16")


if __name__ == "__main__":
    unittest.main()
