from manim import *
class WriteText(Scene): 
    def construct(self): 
        self.camera.background_color = "#ece6e2"
        # 用于设置背景色
        text = Tex("A Text $x=3 \\ 2x =6$")
        text.to_edge(UP)
        text.to_edge(0.0001 * UP )
        self.play(Write(text), run_time=2)
        self.wait(1)
        self.remove(text) # 这个加不加其实影响不大
from manim import *

class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)
class ArrangeObjects(Scene):
    def construct(self):
        text1 = MathTex(r"\frac{d}{dx}f(x)=\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}.")
        text2 = Text("text2 text2")
        text3 = Text("text3 text3 text3")
        textgroup = VGroup(text1, text2, text3)
        textgroup.arrange(
            UP,
            aligned_edge=LEFT,
            buff=0.0
        )
        self.add(textgroup)
        self.wait()

class AngleScene(Scene):
    def construct(self):
        rotation_center = LEFT

        theta_tracker = ValueTracker(110)
        line1 = Line(LEFT, RIGHT)
        line_moving = Line(LEFT, RIGHT)
        line_ref = line_moving.copy()
        line_moving.rotate(theta_tracker.get_value() * DEGREES, about_point=rotation_center)
        a = Angle(line1, line_moving, radius=0.5, other_angle=False)
        tex = MathTex(r"\theta").move_to(
            Angle(
                line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
            ).point_from_proportion(0.5)
        )

        theta_tex = Tex(
            r"$\theta = $",
            str(int(theta_tracker.get_value())),
            r"$^\circ$",
            font_size=50,
            color=RED,
        ).shift(UP * 2)

        self.add(line1, line_moving, a, tex, theta_tex)
        self.wait()

        line_moving.add_updater(
            lambda x,dt: x.become(line_ref.copy()).rotate(
                theta_tracker.get_value() * DEGREES, about_point=rotation_center
            )
        )
        a.add_updater(
            lambda x: x.become(Angle(line1, line_moving, radius=0.5, other_angle=False))
        )
        tex.add_updater(
            lambda x: x.move_to(
                Angle(
                    line1, line_moving, radius=0.5 + 3 * SMALL_BUFF, other_angle=False
                ).point_from_proportion(0.5)
            )
        )
        theta_tex.add_updater(
            lambda x: x.become(
                Tex(
                    r"$\theta = $",
                    str(int(theta_tracker.get_value())),
                    r"$^\circ$",
                    font_size=50,
                    color=RED,
                ).shift(UP * 2)
            )
        )

        self.play(theta_tracker.animate.set_value(90))
        self.play(theta_tracker.animate.increment_value(140), run_time=3)
