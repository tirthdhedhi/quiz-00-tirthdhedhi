"""problem_01.py - mathematical fundamentals (10 points / 40 points)

Uncomment the selected line to make the unit tests pass. Each question only
has one correct answer. Do not uncomment multiple lines. Each function is
a discrete part of the problem. Problem parts do not depend on each other.
If you get stuck, move on and come back. This question will be auto-graded.

**TIP**: To uncomment multiple lines in VS Code, highlight them and use
`Ctrl` + `/`.

Functions:
    problem_01_part_a: tests basic linear algebra knowledge.
    problem_01_part_b: tests basic linear algebra knowledge.
"""

import numpy as np


def problem_01_part_a() -> float:
    """Problem 01 - Part A (5 points).

    Uncomment the line which is approximately equivalent to finding the
    maximum value of x.

    Returns:
        The approximate maximum value of x.
    """
    max_x: float = 0.0
    x: np.ndarray = np.array([0.1, 0.2, 0.5, 0.3, 0.4])

    # Choice A:
    # max_x = np.power(np.sum(np.power(np.abs(x), 2)), 1 / 2)

    # Choice B:
    # max_x = np.power(np.sum(np.power(np.abs(x), 1000)), 1 / 1000)

    # Choice C:
    # max_x = np.argmax(x)

    print(f"Problem 01-A answer: the max of {x} is {max_x}")

    return max_x


def problem_01_part_b() -> float:
    """Problem 01 - Part B (5 points)

    Uncomment the lines which correctly take the dot product of the two
    vectors, x1 and x2.

    Returns:
        The dot product of the two vectors.
    """
    dot_x: float = 0.0

    # Choice A
    # x1: np.ndarray = np.array([1, 2, 5, 3, 4])
    # x2: np.ndarray = np.array([1, 4, 8, 2, 1])
    # dot_x = x1 @ x2

    # Choice B
    # x1: list = [1, 2, 5, 3, 4]
    # x2: list = [1, 4, 8, 2, 1]
    # dot_x = np.sum(np.array(x1 + x2))

    # Choice C
    # x1: np.ndarray = np.array([1, 2, 5, 3, 4])
    # x2: np.ndarray = np.array([1, 4, 8, 2, 1])
    # dot_x = x1 * x2

    print(f"Problem 01-B answer: dot product of x1 and x2 is {dot_x}")

    return dot_x


if __name__ == "__main__":
    problem_01_part_a()
    problem_01_part_b()
