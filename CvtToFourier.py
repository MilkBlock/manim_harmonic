# For python code, firstly use manim to generate a png of function: e^{x}+3x and then use Sympy library to determine
# the laplace transformation of the function.
from manimlib import *

class ExpFunc(Scene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -10,
        "y_max": 10,
        "graph_origin": ORIGIN,
        "function_color": RED,
        "axes_color": GREEN,
    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(lambda x: np.exp(x) + 3 * x, self.function_color)
        self.play(ShowCreation(func_graph))
        self.wait()


