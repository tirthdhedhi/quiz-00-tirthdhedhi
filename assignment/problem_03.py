"""problem_03.py - Classes and neural network fundamentals (10/40 points)

Read through the program and read all comments very carefully! Only uncomment
the code below choices. There is no need to change any other code.

Uncomment the selected line to make the unit tests pass. Each question only
has one correct answer. Do not uncomment multiple lines. Each function is
a discrete part of the problem. Problem parts do not depend on each other.
If you get stuck, move on and come back. This question will be auto-graded.

**TIP**: To uncomment multiple lines in VS Code, highlight them and use
`Ctrl` + `/`.

Functions:
    problem_03_part_a: tests basic knowledge of how Python classes work while
        also testing some practical machine learning knowledge.
    problem_03_part_b: tests more basic knowledge of how Python classes work.
"""

# Define standard imports - nothing special is happening here
import numpy as np
from numpy.typing import NDArray

# Here we import some custom functions to generate and visualize data. We do
# not need to worry about these functions much for the purposes of this quiz.
from assignment.data_generators import generate_xor_dataset
from assignment.data_visualizers import (
    plot_2d_decision_surface_and_features,
    scatter_plot_dataset,
)


# This class implements a simple neural network. **You will need to modify it
# by uncommenting your lines of choice.**
class ToyNeuralNetwork:
    """Implements a toy neural network for academic exercises."""

    def __init__(self) -> None:
        """Initialize a toy neural network."""
        self.bias_hidden: NDArray[np.float64] = np.array([0, 0])
        self.weights_hidden: NDArray[np.float64] = np.array([[1, -1], [-1, 1]])
        self.weights_output: NDArray[np.float64] = np.array([1, 1])
        self.bias_output: float = 0

    def forward(self, x_input: NDArray[np.float64]) -> NDArray[np.float64]:
        """Pass data through the toy neural network."""
        print("Computing inference...")
        layer1_linear = x_input @ self.weights_hidden + self.bias_hidden
        layer1_output = self._activation_function(layer1_linear)
        layer2_linear = layer1_output @ self.weights_output + self.bias_output
        y_output = self._activation_function(layer2_linear)

        print(f"\nLayer 1 Input:\n{x_input}")
        print(f"\nLayer 1 Linear Transformation:\n{layer1_linear}")
        print(f"\nLayer 1 Output:\n{layer1_output}")
        print(f"\nLayer 2 Linear Transformation:\n{layer2_linear}")
        print(f"\nLayer 2 Output:\n{y_output}")

        return y_output

    def _activation_function(self, x: NDArray[np.float64]) -> NDArray[np.float64]:
        """Defines the activation function."""

        # Problem 03 - Part A (5 points)
        #
        # Select the activation function that will make the neural network
        # solve the problem by uncommenting the line(s) for your selection.
        # Use the plot in ./nn_output.jpg to visualize the

        # Choice A
        # y = x

        # Choice B
        # y = 3 * x + 2

        # Choice C
        y = np.maximum(0, x)

        # Choice D
        # print(x.shape)
        # y = np.apply_along_axis(
        #    np.convolve, axis=0, arr=x, v=np.ones(10), mode="same"
        # )

        return y


# This class is a child of the class above. **You will need to modify it by
# uncommenting the lines of your choice.**
class ChildToyNeuralNet(ToyNeuralNetwork):
    # Problem 03 - Part B (5 points)
    #
    # Select the __init__ definition that will perform all the initialization
    # instructions from the parent function and set the weights_hidden
    # variable to all ones.

    # Choice A:
    def __init__(self):
        super().__init__()
        self.weights_hidden = np.array([[1, 1], [1, 1]])

    # Choice B:
    # def __init__(self):
    #     self.weights_hidden = np.array([[1, 1], [1, 1]])

    def _activation_function(self, x: NDArray[np.float64]) -> NDArray[np.float64]:
        """Defines the activation function."""
        return 1 / (1 + np.exp(-x))


# The output of this function will be correct as long as you edited the class
# properly.
def problem_03_part_a(nn, x_features):
    y_predicted = nn.forward(x_features)
    return y_predicted


# The output of this function will be correct as long as you edited the class
# properly.
def problem_03_part_b(child_nn):
    return child_nn.weights_hidden


if __name__ == "__main__":
    # Set the seed for numpy's random number generator so our results are
    # repeatable. DO NOT CHANGE THIS VALUE DURING THE QUIZ.
    np.random.seed(42)

    # Here we generate a classical machine learning dataset. Knowing about the
    # dataset is not important for this quiz if you are not yet familiar with
    # the XOR problem. The XOR problem simply asks us to learn a function,
    #
    # y = f(x1, x2)
    #
    # where f(0,0) = 0, f(1,1) = 0, f(1,0) = 1, and f(0,1) = 1. This is a
    # noteworthy function since there is no such single matrix multiplication
    # operation, f(x1, x2) = A * [x1, x2] + b, that will yield the desired
    # outputs.
    x_features, y_labels, _ = generate_xor_dataset(2, sigma=0.0)

    # View this plot in ./dataset.jpg to see the example data we have
    scatter_plot_dataset(x_features, y_labels, x_plot_dimension=0, y_plot_dimension=1)

    # Here we instantiate a neural network from our class
    nn = ToyNeuralNetwork()
    child_nn = ChildToyNeuralNet()

    # This line plots the output of our neural network as a surface. This
    # should help you decide which choice to make for problem 03 - part A. You
    # can see the visual in ./nn_output.jpg.
    plot_2d_decision_surface_and_features(
        x_features,
        y_labels,
        x_range=(-2, 2),
        y_range=(-2, 2),
        n_grid_points=25,
        plot_function=nn.forward,
    )

    problem_03_part_a(nn, x_features)
    problem_03_part_b(child_nn)
