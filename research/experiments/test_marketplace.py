import unittest
from marketplace import evolve, sigmoid

class MarketplaceTests(unittest.TestCase):
    def test_no_feedback(self):
        self.assertAlmostEqual(evolve(.9,0)['users'],sigmoid(-4))
    def test_bistability(self):
        low=evolve(.05,8)['users']; high=evolve(.95,8)['users']
        self.assertLess(low,.1); self.assertGreater(high,.9)
    def test_full_portability_removes_feedback(self):
        self.assertAlmostEqual(evolve(.9,10,1)['users'],sigmoid(-4))
    def test_convergence_and_invalid(self):
        self.assertLess(evolve(.95,8)['fixed_point_residual'],1e-10)
        with self.assertRaises(ValueError): evolve(.5,portability=1.1)
        with self.assertRaises(ValueError): evolve(.5,steps=-1)
