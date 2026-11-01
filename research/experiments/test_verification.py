import unittest
from verification import compare

class VerificationTests(unittest.TestCase):
    def test_perfect_free_check(self):
        r=compare(.5,0,0,100,0,0)
        self.assertEqual(r['checked_expected_cost_and_loss'],0)
        self.assertEqual(r['unchecked_expected_loss'],50)
    def test_useless_check_adds_cost(self):
        self.assertAlmostEqual(compare(.5,1,0,100,2,0)['net_reduction'],-2)
    def test_false_rejections_cost(self):
        self.assertEqual(compare(1,0,1,100,2,3)['checked_expected_cost_and_loss'],5)
    def test_invalid(self):
        with self.assertRaises(ValueError): compare(.5,0,0,-1,1,1)
