"""Test problem_02.py"""

import numpy as np
import pytest

from assignment.problem_02 import problem_02_part_a, problem_02_part_b


def test_problem_02_part_a():
    """Test problem 01 - Part A."""
    max_x = problem_02_part_a()
    assert max_x == pytest.approx(23.2080327936)


def test_problem_02_part_b():
    """Test problem 01 - Part B."""
    dot_x = problem_02_part_b()
    assert dot_x == pytest.approx(np.array([0, 0, 0, 0, 0, 0, 1, 2, 3, 4]))
