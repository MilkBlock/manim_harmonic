import colorsys
from manim import *

class SimpleText(Scene):
    def construct(self):
        # 创建一个简单的文本对象
        simple_text = Text("Hello, Manim!", font_size=48)
        simple_text.shift(RIGHT*2 + DOWN*2)

        # 在屏幕上显示文本
        self.play(Write(simple_text))
        simple_text2 = Text("Hello, Manim!", font_size=48)
        simple_text2.align_to(simple_text,DL)
        self.play(Write(simple_text2))
        # 等待一段时间
        self.wait(2)

class ComplexFunction(Scene):
    def construct(self):
        axes = ComplexPlane(
            x_range=[-10, 10],
            y_range=[-10, 10],
            axis_config={"color": BLUE},
        )

        func_graph = axes.plot(lambda z: 1/z, color=WHITE)

        self.play(Create(axes), Create(func_graph))
        self.wait(3)
from manim import *

import cmath
class ComplexVectorField(Scene):
    def construct(self):
        # axes = ComplexPlane(
            # x_range=[-3, 3],
            # y_range=[-3, 3],
            # axis_config={"color": BLACK},
        # )  # 这个仅仅是用来生成 坐标轴的，

        def f1(z):
            # if z == 0+0j :
            #     return 0+0j
            # print("input",z)
            # print("output",m)
            return cmath.cos(z)
        def f2(z):
            # z[0] -= 0.75 
            # z[1] -= 0.75 
            return cmath.cosh(z)
        def f3(z):
            return cmath.cosh(1j*z)
            

        v1 = ArrowVectorField(complex_func_to_R3_func(f1),x_range=[-6,6,0.5],y_range=[-3,3,0.5], length_func=lambda l: 0.4)
        # vector_field_1.shift(LEFT*5)

        v2 = ArrowVectorField(complex_func_to_R3_func(f2),x_range=[-6,6,0.5],y_range=[-3,3,0.5], length_func=lambda l: 0.4)
        v3 = ArrowVectorField(complex_func_to_R3_func(f3),x_range=[-6,6,0.5],y_range=[-3,3,0.5], length_func=lambda l: 0.4)
        # vector_field_2.shift(LEFT*5)
        # self.play(Create(axes), Create(vector_field))
        self.play( Create(v1))
        self.wait(1)
        self.play( FadeOut(v1))
        self.play( Create(v2))
        self.wait(1)
        self.play( FadeOut(v2))
        self.play( Create(v3))
        self.wait(1)
        self.play( FadeOut(v3))
        # self.wait(1)
        # self.play(Transform(vector_field_1,vector_field_3))
        # self.play(FadeOut(vector_field_3))


from manim import *

class ComplexMath(Scene):
    def construct(self):
        # Create complex numbers
        z1 = 2 + 3j
        z2 = 4 - 5j

        # Compute the product z1 * z2
        product = z1 * z2

        # Compute the quotient z1 / z2
        quotient = z1 / z2

        # Display the complex numbers and results
        z1_text = MathTex(f"z_1 = {z1}").shift(2 * LEFT)
        z2_text = MathTex(f"z_2 = {z2}").shift(2 * RIGHT)
        product_text = MathTex(rf"z_1 \cdot z_2 = { {product} }").shift(2 * LEFT).shift(1 * DOWN)
        quotient_text = MathTex(rf"\frac{{z_1}}{{z_2}} =  {quotient:.2f} ").shift(2 * RIGHT).shift(2 * DOWN)

        self.play(Write(z1_text), Write(z2_text))
        self.wait(1)
        self.play(Write(product_text), Write(quotient_text))
        self.wait(2)

from manim import *
import numpy as np
from colour import Color

class ComplexFunctionScene(Scene):
    def construct(self):
        plane = ComplexPlane(
            axis_config={"color": BLUE},
        ).add_coordinates()
        
        self.add(plane) # This adds the ComplexPlane to our scene

        # Now, we'll define the complex function itself
        def func(z):
            return 1 / (1 - np.exp(z))

        # This part of the code colors our ComplexPlane according to the function
        step_size = 0.5
        for x in np.arange(*plane.x_range):
            for y in np.arange(*plane.y_range):
                z = complex(x, y)
                w = func(z)
                
                # We convert the output to a color where the phase is the hue and the magnitude is the saturation
                phase = np.angle(w) / (2 * PI)
                magnitude = np.log2(1 + abs(w))
                color = colorsys.hsv_to_rgb(phase, magnitude, 1)
                c = Color(); c.set_rgb(color)

                dot = Dot(plane.coords_to_point(x, y), color=c)
                dot.set_z_index(-1)  # This makes sure the dots are behind the plane axes
                self.add(dot)

        self.wait(1)

from manim import *

class HexagonScene(Scene):
    def construct(self):
        # 创建一个六边形
        m=[complex_to_R3(np.exp(2*np.pi*1j/6*i+ np.pi/12*1j ) + 0.5+ 0.5j ) for i in range(6)]
        hexagon = Polygon(
            *m,
            stroke_color=WHITE,
            fill_color=BLUE,
            fill_opacity=0.5
        )
        print(m)
        m1=list(map(lambda x: complex_to_R3(complex(x[0],x[1])**3),m))
        print(m1)
        hexagon1 = Polygon(
            *m1,
            stroke_color=WHITE,
            fill_color=BLUE,
            fill_opacity=0.5
        ) # type: ignore
        center = sum(m)/len(m)
        center_proj = complex_to_R3(complex(center[0],center[1])**3)
        center1 = sum(m1)/len(m1)
        center_point1 = Dot(point=center1,color=ORANGE)
        center_point_proj = Dot(point=center_proj,color=RED)

        origin_point = Dot(point=ORIGIN, color=RED)
        origin_label = Text("O").scale(0.5).next_to(origin_point, DOWN)
        self.add(hexagon)
        self.add(origin_point,origin_label)
        self.play(Transform(hexagon,hexagon1),Transform(origin_point,center_point1),Transform(origin_label,Text("predicted").scale(0.5).next_to(center1,DOWN)))
        self.wait(0.5)
        # self.add(origin_point, origin_label)
        self.add(center_point_proj,Text("projeted").scale(0.5).next_to(center_point_proj, DOWN))

        # 将六边形添加到场景中

        # 保持画面
        self.wait(2)

from manim import *

class MarkOrigin(Scene):
    def construct(self):
        # 创建原点的标记，例如一个小红点
        origin_point = Dot(point=ORIGIN, color=RED)
        origin_point1 = Dot(point=np.array([1,2,0]), color=RED)

        # 创建一个标签来标识原点，例如文字 "O"
        origin_label = Text("O").scale(0.5).next_to(origin_point, DOWN)
        origin_label1 = Text("R").scale(0.5).next_to(origin_point1, DOWN)

        # 将原点标记和标签添加到场景
        self.add(origin_point, origin_label)
        self.add(origin_point1, origin_label1)

        # 暂停几秒钟以展示场景
        self.wait(2)

# 保存此文件并在命令行运行以下命令来生成视频：
# manim -p -ql your_script_name.py MarkOrigin

from manim import *

# 1/z 变换函数
def transform_z(z):
    return 1/z

class CircleToTransform(Scene):
    def construct(self):
        # 创建一个圆
        a = 1+3j
        def mobius(z):
            return (z-a) / (a.conjugate()*z - 1 )
        

        circle = Circle()#.move_arc_center_to(point = complex_to_R3(2+2j))
        self.play(Create(circle))
        self.wait(1)

        # 创建用于 1/z 变换的坐标轴
        axes = Axes(
            x_range=[-4, 4, 0.25],
            y_range=[-2, 2, 0.25],
            x_length=8,
            y_length=4
        )
        self.play(Create(NumberPlane()))
        self.wait(1)

        # 将圆映射到新的 1/z 变换位置
        # transformed_circle = circle.copy().apply_function(lambda p: complex_to_R3(transform_z(R3_to_complex(p))))
        transformed_circle = circle.copy().apply_function(complex_func_to_R3_func(mobius))
        self.play(Transform(circle, transformed_circle))
        self.wait(1)

# 当在命令行中运行这个脚本时，确保使用以下命令来生成视频：
# manim -pql script.py CircleToTransform

