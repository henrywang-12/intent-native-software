"""Illustrative platform economics; synthetic assumptions, no company estimates.

Run: python3 research/experiments/test_platform_power.py
Existing research CI discovers this module and executes its invariant tests.
"""
import math
import unittest


def nonnegative(value):
    if not math.isfinite(value) or value < 0:
        raise ValueError("expected a finite nonnegative value")
    return value


def break_even_tasks(fixed_cost, contribution):
    """Minimum integer tasks covering fixed cost; None if positive cost cannot be covered."""
    fixed_cost = nonnegative(fixed_cost)
    if not math.isfinite(contribution):
        raise ValueError("expected finite contribution")
    if fixed_cost == 0:
        return 0
    if contribution <= 0:
        return None
    return math.ceil(fixed_cost / contribution)


def net_value(tasks, margin, fixed_cost, per_task_fee, support_per_task):
    """Contribution after declared costs; excludes unmodeled acquisition and taxes."""
    if not isinstance(tasks, int) or isinstance(tasks, bool) or tasks < 0:
        raise ValueError("tasks must be a nonnegative integer")
    for value in (margin, fixed_cost, per_task_fee, support_per_task):
        nonnegative(value)
    return tasks * (margin - per_task_fee - support_per_task) - fixed_cost


def concentration(shares):
    """Normalized-share HHI, range 1/n..1; not a legal market-power test."""
    values = list(shares)
    if not values:
        raise ValueError("at least one share required")
    for value in values:
        nonnegative(value)
    total = sum(values)
    if total <= 0 or not math.isfinite(total):
        raise ValueError("positive finite total required")
    return sum((value / total) ** 2 for value in values)


def completion_given_conditional_rates(rates):
    """Chain rule: each probability is conditional on ALL previous stages succeeding.

    Supplying unconditional marginal rates would require an independence assumption.
    """
    result = 1.0
    for rate in rates:
        nonnegative(rate)
        if rate > 1:
            raise ValueError("probability exceeds one")
        result *= rate
    return result


class PlatformPowerTests(unittest.TestCase):
    def test_break_even_rounds_up(self):
        self.assertEqual(break_even_tasks(101, 10), 11)

    def test_no_positive_margin(self):
        self.assertIsNone(break_even_tasks(100, 0))
        self.assertIsNone(break_even_tasks(100, -1))
        self.assertEqual(break_even_tasks(0, 0), 0)

    def test_shared_runtime_can_help_or_hurt(self):
        standalone = net_value(100, 10, 600, 0, 1)
        shared = net_value(100, 10, 100, 2, 1)
        expensive = net_value(100, 10, 100, 8, 1)
        self.assertGreater(shared, standalone)
        self.assertLess(expensive, standalone)

    def test_fixed_cost_crossover(self):
        # Savings of 500 are exhausted at 250 tasks with a fee difference of 2.
        self.assertEqual(net_value(250, 10, 600, 0, 1),
                         net_value(250, 10, 100, 2, 1))

    def test_hhi_endpoints_and_scale(self):
        self.assertEqual(concentration([1]), 1)
        self.assertEqual(concentration([1, 1, 1, 1]), 0.25)
        self.assertAlmostEqual(concentration([20, 80]), concentration([0.2, 0.8]))

    def test_concentration_rises_when_shares_unequal(self):
        self.assertGreater(concentration([0.9, 0.1]), concentration([0.5, 0.5]))

    def test_conditional_chain(self):
        self.assertAlmostEqual(completion_given_conditional_rates([0.9, 0.8, 0.5]), 0.36)
        self.assertEqual(completion_given_conditional_rates([1, 0, 1]), 0)
        self.assertEqual(completion_given_conditional_rates([]), 1)

    def test_improving_stage_cannot_hurt_completion(self):
        self.assertGreaterEqual(completion_given_conditional_rates([0.9, 0.95]),
                                completion_given_conditional_rates([0.9, 0.8]))

    def test_reject_invalid_inputs(self):
        for value in (-1, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                break_even_tasks(value, 1)
            with self.assertRaises(ValueError):
                concentration([value, 1])
            with self.assertRaises(ValueError):
                completion_given_conditional_rates([value])
        with self.assertRaises(ValueError):
            completion_given_conditional_rates([1.1])
        for shares in ([], [0, 0]):
            with self.assertRaises(ValueError):
                concentration(shares)
        for tasks in (-1, 1.5, True):
            with self.assertRaises(ValueError):
                net_value(tasks, 10, 100, 1, 1)


if __name__ == "__main__":
    unittest.main()
