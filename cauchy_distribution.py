from cmath import pi
import manim_prelude
from manim import *
import numpy as np
class ExampleFunctionGraph(Scene):
    def construct(self):
        cos_func = FunctionGraph(
            lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
            color=RED,
        )

        sin_func_1 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            color=BLUE,
        )

        sin_func_2 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            x_range=[-4, 4],
            color=GREEN,
        ).move_to([0, 1, 0])

        self.add(cos_func, sin_func_1, sin_func_2)

class cauchy_distribution(Scene):
    def construct(self):
        # 把特征向量转换为Manim的Vector格式
        # arrows,texts,tags= manim_prelude.generate_arrow_and_text_from_sympy_matrix(eigenvectors,is_updater_on=True)
        p1 = NumberPlane()

        cauchy_dis_f = FunctionGraph(
            f:=lambda x: 1/pi * (np.arctan(x) +  pi/2)
        )
        cauchy_ = FunctionGraph(
            g:=lambda x: 1/(1+x**2)
        )
        b_fname = Tex("Cauchy distribution",font_size =75 )
        b_fname.move_to([-3,-3,0])
        self.play(FadeIn(cauchy_dis_f),FadeIn(b_fname),FadeIn(p1))
        self.wait(2)
        self.play(FadeOut(cauchy_dis_f),FadeOut(b_fname))
        # graph = (*arrows,p1,*texts,*tags)
        # self.play(*[Create(mob) for mob in graph],
        #             Create(b_Before),
        #             )
        # self.wait(1)

        # # 对平面应用线性变换M
        # self.play(Transform(b_Before,b_After))
        # matrix_transform = np.array(M_values).astype(float)
        # self.play(*(ApplyMatrix(matrix_transform, mob) for mob in (*arrows,p1)))
        # self.play(Create(b_Cause))

        # self.wait(4)




from manim import *

class QuadraticGraph(Scene):
    def construct(self):
        # Create a plane with axis and labels
        plane = NumberPlane(
            x_range=[-10, 10, 1],  # X axis range
            y_range=[-5, 5, 1],    # Y axis range
            x_length=10,           # Width of the plane
            y_length=6             # Height of the plane
        ).add_coordinates()        # Add the x and y axis labels

        # Define the quadratic function
        def quadratic_function(x):
            return 0.5 * x ** 2  # Change the coefficient for a steeper or wider parabola

        # Create the graph of the quadratic function
        graph = plane.plot(quadratic_function, color=BLUE)

        # Create labels for the graph
        graph_label = MathTex("y=0.5x^2").next_to(graph, UP)

        # Display everything
        self.play(Create(plane))
        self.play(Create(graph), Write(graph_label))
        self.wait()
