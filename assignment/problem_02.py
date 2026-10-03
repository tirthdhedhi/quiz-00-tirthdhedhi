"""problem_02.py - linear and nonlinear functions (10 points / 40 points)

Uncomment the selected line to make the unit tests pass. Each question only
has one correct answer. Do not uncomment multiple lines. Each function is
a discrete part of the problem. Problem parts do not depend on each other.
If you get stuck, move on and come back. This question will be auto-graded.

**TIP**: To uncomment multiple lines in VS Code, highlight them and use
`Ctrl` + `/`.

Functions:
    problem_02_part_a: tests basic linear and nonlinear function knowledge.
    problem_02_part_b: tests basic linear and nonlinear function knowledge.
"""

import numpy as np


def problem_02_part_a() -> np.ndarray:
    """Problem 02 - Part A (5 points).

    Uncomment the line(s) which computes a **linear** function of x.

    Returns:
        The linear function applied to x.
    """
    np.random.seed(42)
    x: np.ndarray = np.arange(0, 10)
    fx: np.ndarray = np.zeros(x.shape)

    # Choice A:
    w: np.ndarray = np.random.random(x.shape)
    fx = np.sum(w * x)

    # Choice B:
    # fx = x**2

    # Choice C:
    # fx = np.sin(w*x)

    print(f"Problem 02-A answer: x = {x}, f(x) = {fx}")

    return fx


def compute_rectified_linear_unit(x: np.ndarray) -> np.ndarray:
    """Compute a rectified linear unit on the input."""
    return np.maximum(0, x)


def problem_02_part_b() -> np.ndarray:
    """Problem 02 - Part A (5 points).

    Uncomment the line(s) which computes a **nonlinear** function of x.

    Pay attention to the details!

    Returns:
        The linear function applied to x.
    """
    x: np.ndarray = np.arange(-5, 5)
    fx: np.ndarray = np.zeros(x.shape)

    # Choice A:
    # w: np.ndarray = np.random.random(x.shape)
    # fx = np.trapz(w * x)

    # Choice B:
    # fx = np.dot(w, x)

    # Choice C:
    fx = compute_rectified_linear_unit(x)

    print(f"Problem 02-B answer: x = {x}, f(x) = {fx}")

    return fx


if __name__ == "__main__":
    problem_02_part_a()
    problem_02_part_b()
