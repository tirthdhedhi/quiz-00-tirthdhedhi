"""Test problem_03.py"""

import numpy as np
import pytest

from assignment.data_generators import generate_xor_dataset
from assignment.problem_03 import (
    ChildToyNeuralNet,
    ToyNeuralNetwork,
    problem_03_part_a,
    problem_03_part_b,
)


def test_problem_03_part_a():
    np.random.seed(42)
    x_features, _, _ = generate_xor_dataset(2, sigma=0.0)
    nn = ToyNeuralNetwork()
    y_predicted = problem_03_part_a(nn, x_features)
    assert y_predicted == pytest.approx(np.array([0, 0, 1, 1]))


def test_problem_03_part_b():
    child_nn = ChildToyNeuralNet()
    assert problem_03_part_b(child_nn) == pytest.approx(np.ones((2, 2)))
