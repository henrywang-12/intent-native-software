import unittest
from retry import risk

class RetryTests(unittest.TestCase):
    def test_blind_retry(self):
        r=risk(.5,0,.8)
        self.assertEqual(r['blind_retry_duplicate_probability'],.5)
        self.assertAlmostEqual(r['read_then_retry_on_missing_duplicate_probability'],.1)
        self.assertAlmostEqual(r['read_only_unresolved_probability'],.6)
    def test_perfect_deduplication(self):
        self.assertEqual(risk(1,1,0)['blind_retry_duplicate_probability'],0)
    def test_absence_not_resolved(self):
        self.assertEqual(risk(0,1,1)['read_only_unresolved_probability'],1)
    def test_invalid(self):
        with self.assertRaises(ValueError): risk(.5,2,.8)
