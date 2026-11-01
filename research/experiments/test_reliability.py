import unittest
from reliability import completion

class ReliabilityTests(unittest.TestCase):
    def test_known_product(self):
        self.assertAlmostEqual(completion(.5,3), .125)
        self.assertAlmostEqual(completion(.5,3,.2), .1)
    def test_empty_workflow(self):
        self.assertEqual(completion(0,0,1),1)
    def test_bounds(self):
        self.assertEqual(completion(1,20,1),0)
        for args in ((float('nan'),2),(.5,-1),(.5,True),(.5,2,1.1)):
            with self.assertRaises(ValueError): completion(*args)
    def test_monotonicity(self):
        self.assertLess(completion(.98,20),completion(.98,10))
