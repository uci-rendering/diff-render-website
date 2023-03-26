from manim import *
from manim.utils.color import Colors
import numpy as np

config.background_color = WHITE

def init_axis(x_range, y_range, length=1., precision=0):
    ax = Axes(
        x_range = x_range,
        y_range = y_range,
        x_length = length*(x_range[1] - x_range[0]),
        y_length = length*(y_range[1] - y_range[0]),
        tips = False,

        axis_config = {
            "color": Colors.light_gray.value,
            # "include_numbers": True,
            "include_ticks": True,
            "decimal_number_config": {
                "num_decimal_places": precision,
                "color": Colors.light_gray.value,
            },
            "font_size": 32
        },

        x_axis_config = {
            "include_numbers": True,
            "numbers_to_include": np.arange(0., 1.01, .2),
        },           
    )
    labels = ax.get_axis_labels(x_label="x", y_label="f").set_color(Colors.light_gray.value)
    return ax, labels


class SuccessExample_Base(Scene):
    def __init__(self):
        super().__init__()
        self.ax, labels = init_axis((-.1, 1.2, .1), (-.1, .6, .1), length=10., precision=1)
        self.add(self.ax, labels)

    def get_plot(self, func, clr, theta_txt, dir):
        graph = self.ax.plot(func, x_range=[0., 1.], color=clr)
        label = self.ax.get_graph_label(graph, x_val=1., direction=dir, label="f(x, " + theta_txt + ")").scale(.8)
        area = self.ax.get_area(graph, x_range=[0., 1.], color=clr, opacity=.3).set_stroke(opacity=0.)
        area_label = MathTex("I(" + theta_txt + ")", color=clr).move_to(self.ax.c2p(.8, .4*func(.8)))
        return graph, label, area, area_label


class SuccessExample_0(SuccessExample_Base):
    def __init__(self):
        super().__init__()
        self.t0 = .35
        self.f0 = lambda x: self.t0*x*x

    def construct(self):
        graph0, label0, area0, area0_label = self.get_plot(self.f0, BLUE, r"\theta_0", UR*.25)
        self.add(graph0, label0, area0, area0_label)


class SuccessExample_1(SuccessExample_0):
    def __init__(self):
        super().__init__()
        self.dt = .15
        self.f1 = lambda x: (self.t0 + self.dt)*x*x

    def construct(self):
        graph0, label0, _, _ = self.get_plot(self.f0, BLUE, r"\theta_0", UR*.25)
        graph0.set_stroke(opacity = .5)
        self.add(DashedVMobject(graph0, num_dashes=30), label0)

        graph1, label1, area1, area1_label = self.get_plot(self.f1, RED, r"\theta_0 + \Delta\theta", UR*.25)
        self.add(graph1, label1, area1, area1_label)


class SuccessExample_2(SuccessExample_1):
    def __init__(self):
        super().__init__()

    def construct(self):
        graph0, label0, _, _ = self.get_plot(self.f0, BLUE, r"\theta_0", UR*.25)
        graph1, label1, _, _ = self.get_plot(self.f1, RED, r"\theta_0 + \Delta\theta", UR*.25)
        d_area = self.ax.get_area(graph0, x_range=[0., 1.], bounded_graph=graph1, color=ORANGE, opacity=0.3).set_stroke(opacity = 0.)
        self.add(d_area, graph0, label0, graph1, label1)

        arrow_x = .675
        arrow_y = .5*(self.f0(arrow_x) + self.f1(arrow_x))
        arrow = Arrow(self.ax.c2p(arrow_x - .2, arrow_y), self.ax.c2p(arrow_x, arrow_y), buff=0., color=ORANGE, max_tip_length_to_length_ratio=.1)
        self.add(arrow)

        d_area_label = MathTex(r"I(\theta_0 + \Delta\theta) - I(\theta_0)", color=ORANGE)
        d_area_label.scale(.8).next_to(arrow.get_start(), direction=LEFT)
        self.add(d_area_label)

        x0 = .9
        line = self.ax.get_vertical_line(self.ax.i2gp(x0, graph1), color=GRAY)
        self.add(line)

        dot0 = Dot(self.ax.c2p(x0, 0.), color=GRAY).scale(.8)
        dot1 = Dot(self.ax.c2p(x0, self.f0(x0)), color=BLUE).scale(.8)
        dot2 = Dot(self.ax.c2p(x0, self.f1(x0)), color=RED).scale(.8)
        self.add(dot0, dot1, dot2)

        dot0_label = MathTex(r"x", color=GRAY).scale(.8).next_to(dot0, direction=.5*DOWN)
        self.add(dot0_label)

        brace = Brace(Line(dot1.get_center(), dot2.get_center()), direction=LEFT, color=BLACK, fill_opacity=.5)
        brace_tex = MathTex(r"f(x, \theta_0 + \Delta\theta) - f(x, \theta_0)\\ \approx \left[\frac{\mathrm{d}}{\mathrm{d}\theta} f(x, \theta)\right]_{\theta = \theta_0} \,\Delta\theta", color=BLACK).scale(.8).set_opacity(.5)
        brace_tex.next_to(brace, LEFT)
        self.add(brace, brace_tex)