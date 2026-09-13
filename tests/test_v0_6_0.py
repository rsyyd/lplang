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

class TestV060Features(unittest.TestCase):

    def test_struct_definition_and_creation(self):
        src = """
        struct Person {
            name
            age
        }
        let p = Person { name: "Renz", age: 30 }
        print p.name
        print p.age
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("Renz", res.stdout)
        self.assertIn("30", res.stdout)

    def test_struct_method_syntax(self):
        src = """
        struct Person {
            name
            age
        }
        fn (p: Person) greet() {
            print "hello ${p.name}"
        }
        let p = Person { name: "Lumpo", age: 1 }
        p.greet()
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("hello Lumpo", res.stdout)

    def test_struct_rejects_unknown_and_missing_fields(self):
        unknown = run_lp("""
        struct Point { x, y }
        let p = Point { x: 1, z: 2 }
        """)
        self.assertNotEqual(unknown.returncode, 0)
        self.assertIn("unknown field 'z'", unknown.stderr)

        missing = run_lp("""
        struct Point { x, y }
        let p = Point { x: 1 }
        """)
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("missing required field 'y'", missing.stderr)

    def test_struct_rejects_unknown_assignment_and_duplicate_fields(self):
        unknown = run_lp("""
        struct Point { x, y }
        let p = Point { x: 1, y: 2 }
        p.z = 3
        """)
        self.assertNotEqual(unknown.returncode, 0)
        self.assertIn("unknown field 'z'", unknown.stderr)

        duplicate = run_lp("""
        struct Point { x, x }
        """)
        self.assertNotEqual(duplicate.returncode, 0)
        self.assertIn("duplicate field 'x'", duplicate.stderr)

    def test_struct_dot_assignment_updates_existing_field(self):
        res = run_lp("""
        struct Point { x, y }
        let p = Point { x: 1, y: 2 }
        p.x += 4
        p.y = 9
        print p.x
        print p.y
        """)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("5", res.stdout)
        self.assertIn("9", res.stdout)

    def test_match_literal_pattern(self):
        src = """
        let x = 5
        match x {
            case 5 => print "five"
            default => print "other"
        }
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("five", res.stdout)

    def test_match_struct_pattern(self):
        src = """
        struct Point { x, y }
        let p = Point { x: 1, y: 2 }
        match p {
            case Point { x: 1, y: 2 } => print "origin-ish"
            default => print "nope"
        }
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("origin-ish", res.stdout)

    def test_match_variable_binding(self):
        src = """
        let val = 42
        match val {
            case n => print "got ${n}"
        }
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("got 42", res.stdout)

    def test_match_case_accepts_block_and_multiple_statements(self):
        src = """
        let val = 2
        match val {
            case 1 {
                let label = "one"
                print label
            }
            default {
                print "other"
            }
        }
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("other", res.stdout)

    def test_match_identifier_can_still_be_bound(self):
        src = """
        let match = 7
        print match
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual(res.stdout.strip(), "7")

    def test_list_comprehension(self):
        src = """
        let nums = [1, 2, 3, 4, 5]
        let doubled = [x * 2 for x in nums if x > 2]
        print join(doubled, ", ")
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("6, 8, 10", res.stdout)

    def test_map_comprehension(self):
        src = """
        let nums = [1, 2, 3]
        let m = { ("k${x}"): x for x in nums }
        print m.k1
        print m.k3
        """
        res = run_lp(src)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertIn("1", res.stdout)
        self.assertIn("3", res.stdout)

if __name__ == '__main__':
    unittest.main()