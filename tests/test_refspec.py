import unittest
from main import parse_refspec, explain

class RefspecTests(unittest.TestCase):
    def test_force_wildcard(self):
        rule = parse_refspec("+refs/heads/*:refs/remotes/origin/*")
        self.assertTrue(rule.force)
        self.assertEqual(explain(["+refs/heads/*:refs/remotes/origin/*"], ["refs/heads/main"]),
                         ["FORCE refs/heads/main -> refs/remotes/origin/main"])

    def test_negative_excludes_matching_ref(self):
        lines = explain(["refs/heads/*:refs/remotes/origin/*", "^refs/heads/private/*"],
                        ["refs/heads/main", "refs/heads/private/demo"])
        self.assertEqual(lines, ["refs/heads/main -> refs/remotes/origin/main"])

    def test_deletion(self):
        self.assertEqual(explain([":refs/heads/old"], []),
                         ["DELETE refs/heads/old (destination removal; no source ref)"])

    def test_mismatched_wildcards_rejected(self):
        with self.assertRaises(ValueError):
            parse_refspec("refs/heads/*:refs/remotes/origin")

if __name__ == "__main__":
    unittest.main()
