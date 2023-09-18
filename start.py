from manim import *
# config.renderer=RendererType.OPENGL   使用这个选项会导致 可能的不完全绘制


from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle(radius=3)  # create a circle
        circle.set_fill(BLUE, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(BLUE, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        circle.set_fill(color=GREEN,opacity=0.5)  # the default value of opacity is 1
        square.set_fill(color=GREEN_A,opacity=0.5)
        square.next_to(circle,buff=0.5)
        self.play(Create(circle),Create(square))
        self.play(FadeOut(circle))
        self.play(FadeOut(square))

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate(run_time = 2 ).rotate(PI / 4),square.animate.shift(RIGHT*2)) # rotate the square
        circle.next_to(square,ORIGIN,buff=0.5)
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen

class AnimateWithArgsExample(Scene):
    def construct(self):
        s = Square()
        c = Circle()

        VGroup(s, c).arrange(RIGHT, buff=2)
        self.add(s, c)

        self.play(
            s.animate(run_time=2).rotate(PI / 2),
            c.animate(rate_func=there_and_back).shift(RIGHT),
        )
        self.play(
            s.animate(run_time=2).rotate(PI / 2),
            c.animate(rate_func=there_and_back_with_pause).shift(RIGHT),
        )
        self.play(
            s.animate(run_time=2).rotate(PI / 2),
            c.animate(rate_func=rush_into).shift(RIGHT),
        )
        self.play(
            s.animate(run_time=2).rotate(PI / 2),
            c.animate(rate_func=rush_from).shift(RIGHT),
        )
        self.play(
            s.animate(run_time=2).rotate(PI / 2),
            c.animate(rate_func=smooth).shift(RIGHT),
        )


class GeometricShapes(Scene):
    def construct(self):
        d = Dot()
        c = Circle()
        s = Square()
        t = Triangle()
        d.next_to(c, RIGHT,buff=1)  # buff指的是间隔，这里默认是0.5
        s.next_to(c, LEFT,buff=1)
        t.next_to(c, DOWN,buff=1)
        self.add(d, c, s, t)


class StartScene(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(Create(square))
        self.wait()

        # 这会打开一个iPython终端，你可以在其中继续写你想要执行的代码
        # 在这个例子中，square/circle/self都会成为终端中的实例
        # self.embed()

        # 尝试拷贝粘贴下面这些行到交互终端中
        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(circle.animate.stretch(4, 0))
        self.play(Rotate(circle, 90 * DEGREES))
        self.play(circle.animate.shift(2 * RIGHT).scale(0.25))

        text = Text("""
            In general, using the interactive shell
            is very helpful when developing new scenes
        """)
        self.play(Write(text))
        self.add()

        # 在交互终端中，你可以使用play, add, remove, clear, wait, save_state
        # 和restore来代替self.play, self.add, self.remove……

        # 这时如果要使用鼠标键盘来与窗口互动，需要输入执行touch()
        # 然后你就可以滚动窗口，或者在按住z时滚动来缩放
        # 按住d时移动鼠标来更改相机视角，按r重置相机位置
        # 按q退出和窗口的交互来继续输入其他代码

        # 特别的，你可以自定一个场景来和鼠标和键盘互动
        always(circle.move_to, self.mouse_drag_point)

class VectorFieldExample(Scene):
    def construct(self):
        matrix = np.identity(2)
        # matrix = np.array(self.matrix)
        def func(pos):
            # return 0.15 * np.dot(matrix.T, [x, y])
            v = np.array([pos[1],-pos[0],1])
            return v/np.linalg.norm(v)

        # plane = NumberPlane()
        vector_field = StreamLines(
            func
            # magnitude_range=(0, 2),
            #vector_config={"thickness": 0.025}

        )
        # self.add(plane, vector_field)
        self.add( vector_field)

class ScaleVectorFieldFunction(Scene):

    def construct(self):
        func = lambda pos: (np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP)/np.linalg.norm((np.sin(pos[1]) * RIGHT + np.cos(pos[0]) * UP))
        vector_field = ArrowVectorField(func,x_range=[ -1,1,1/4 ],y_range=[ -1,1,1/4 ])
        self.add(vector_field)
        self.wait()

        func = VectorField.scale_func(func, 0.5)
        self.play(vector_field.animate.become(ArrowVectorField(func,x_range=[ -1,1,1/4 ],y_range=[ -1,1,1/4 ])))
        self.wait()


class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello 你好', r'$\bigstar$', r'\LaTeX', font_size=90,tex_template=TexTemplateLibrary.ctex)
        tex.set_color_by_tex('igsta', RED)

        self.add(tex)
        
        self.play(tex.animate.shift(RIGHT),rate_func=there_and_back)#,rate_func = not_quite_there)

        
        
class FallingDot(Scene):
    def construct(self):
        def time_func_gen(lateral):
            return lambda t: max(0,min(1,5*(t-lateral)))
        
        def co(t):
            print(t)
            return t
        dot_G = [Group(*[ Dot(j*RIGHT+4*i*RIGHT+8*LEFT) for j in range(3)]) for i in range(4)]  # 共计四组
        for g in dot_G:
            self.add(*g)
    
        # self.play(*[dot.animate(run_time = 5,rate_func =time_func_gen(i*j*0.1)).shift(2*DOWN) for i,g in enumerate(dot_G) for j,dot in enumerate(g)])
        self.play(*[dot.animate(run_time = 5,lateral_rate=0.3,rate_func =co).shift(2*DOWN) for i,g in enumerate(dot_G) for j,dot in enumerate(g)])
        # self.play(*[dot.animate(lag_ratio=i*j*0.5).shift(2*DOWN) for i,g in enumerate(dot_G) for j,dot in enumerate(g)])