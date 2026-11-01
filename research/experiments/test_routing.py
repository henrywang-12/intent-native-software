import unittest
from routing import evaluate

class RoutingTests(unittest.TestCase):
    def test_perfect_checker(self):
        r=evaluate(.5,.8,0,0,1,10,2)
        self.assertAlmostEqual(r['correct_probability'],.9)
        self.assertAlmostEqual(r['expected_cost'],8)
    def test_accept_everything(self):
        r=evaluate(.4,.99,1,0)
        self.assertAlmostEqual(r['correct_probability'],.4)
        self.assertAlmostEqual(r['escalation_probability'],0)
    def test_reject_everything(self):
        self.assertAlmostEqual(evaluate(.4,.8,0,1)['correct_probability'],.8)
    def test_invalid(self):
        with self.assertRaises(ValueError): evaluate(.5,.8,.1,.1,cheap_cost=-1)
        with self.assertRaises(ValueError): evaluate(.5,float('nan'),.1,.1)
