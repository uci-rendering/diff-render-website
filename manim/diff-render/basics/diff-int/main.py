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


class Example_Base(Scene):
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

    def get_piecewise_plot(self, x0, y0, y1, clr, theta_txt):
        graphL = self.ax.plot(lambda x: y0, x_range=[0., x0], color=clr)
        areaL = self.ax.get_area(graphL, x_range=[0, x0], color=clr, opacity=.3).set_stroke(opacity=0.)
        graphR = self.ax.plot(lambda x: y1, x_range=[x0, 1.], color=clr)
        areaR = self.ax.get_area(graphR, x_range=[x0, 1.], color=clr, opacity=.3).set_stroke(opacity=0.)
        area_label = MathTex("I(" + theta_txt + ")", color=clr).move_to(self.ax.c2p(.5, .5*min(y0, y1)))
        line = DashedLine(self.ax.c2p(x0, y0), self.ax.c2p(x0, y1), color=clr)
        return VGroup(graphL, graphR, line), VGroup(areaL, areaR), area_label

class SuccessExample_0(Example_Base):
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


class FailureExample_0(Example_Base):
    def __init__(self):
        super().__init__()
        self.t0 = .5
        self.y0 = .5

    def construct(self):
        graph0, area0, area0_label = self.get_piecewise_plot(self.t0, self.y0, .5*self.y0, BLUE, r"\theta_0")
        label0 = MathTex(r"f(x, \theta_0)", color=BLUE).scale(.8).next_to(self.ax.c2p(self.t0, .75*self.y0), direction=RIGHT)
        self.add(graph0, label0, area0, area0_label)


class FailureExample_1(FailureExample_0):
    def __init__(self):
        super().__init__()
        self.dt = .1

    def construct(self):
        graph0, _, _ = self.get_piecewise_plot(self.t0, self.y0, .5*self.y0, BLUE, r"\theta_0")
        label0 = MathTex(r"f(x, \theta_0)", color=BLUE).scale(.8).next_to(self.ax.c2p(self.t0, .75*self.y0), direction=RIGHT)
        graph0.set_stroke(opacity = .5)
        label0.next_to(self.ax.c2p(self.t0, .75*self.y0), direction=LEFT)
        self.add(graph0, label0)

        graph1, area1, area1_label = self.get_piecewise_plot(self.t0 + self.dt, self.y0, .5*self.y0, RED, r"\theta_0 + \Delta\theta")
        label1 = MathTex(r"f(x, \theta_0 + \Delta\theta)", color=RED).scale(.8).next_to(self.ax.c2p(self.t0 + self.dt, .75*self.y0), direction=RIGHT)
        self.add(graph1, label1, area1, area1_label)


class FailureExample_2(FailureExample_1):
    def __init__(self):
        super().__init__()

    def construct(self):
        graph0, _, _ = self.get_piecewise_plot(self.t0, self.y0, .5*self.y0, BLUE, r"\theta_0")
        label0 = MathTex(r"f(x, \theta_0)", color=BLUE).scale(.8).next_to(self.ax.c2p(self.t0, self.y0), direction=DL)
        graph1, _, _ = self.get_piecewise_plot(self.t0 + self.dt, self.y0, .5*self.y0, RED, r"\theta_0 + \Delta\theta")
        label1 = MathTex(r"f(x, \theta_0 + \Delta\theta)", color=RED).scale(.8).next_to(self.ax.c2p(self.t0 + self.dt, .5*self.y0), direction=DR)

        self.add(Polygon(
            self.ax.c2p(self.t0          , .5*self.y0),
            self.ax.c2p(self.t0 + self.dt, .5*self.y0),
            self.ax.c2p(self.t0 + self.dt,    self.y0),
            self.ax.c2p(self.t0          ,    self.y0),
            stroke_width=0., fill_color=ORANGE, fill_opacity=.3
        ))
        self.add(graph0, label0, graph1, label1)

        arrow_x = self.t0 + .5*self.dt
        arrow_y = .75*self.y0
        arrow = Arrow(self.ax.c2p(arrow_x - .15, arrow_y), self.ax.c2p(arrow_x, arrow_y), buff=0., color=ORANGE, max_tip_length_to_length_ratio=.1)
        self.add(arrow)

        d_area_label = MathTex(r"I(\theta_0 + \Delta\theta) - I(\theta_0)", color=ORANGE)
        d_area_label.scale(.8).next_to(arrow.get_start(), direction=LEFT)
        self.add(d_area_label)

        line0 = self.ax.get_vertical_line(self.ax.i2gp(self.t0, graph0[1]), color=BLUE).set_opacity(.5)
        line1 = self.ax.get_vertical_line(self.ax.i2gp(self.t0 + self.dt, graph1[1]), color=RED).set_opacity(.5)
        self.add(line0, line1)

        dot0 = Dot(self.ax.c2p(self.t0          , 0.), color=BLUE).scale(.8)
        dot1 = Dot(self.ax.c2p(self.t0 + self.dt, 0.), color=RED).scale(.8)
        self.add(dot0, dot1)

        dot0_label = MathTex(r"x(\theta_0)", color=BLUE).scale(.8).next_to(dot0, direction=.5*UL)
        dot1_label = MathTex(r"x(\theta_0 + \Delta\theta)", color=RED).scale(.8).next_to(dot1, direction=.5*UR)
        self.add(dot0_label, dot1_label)

        brace = Brace(
            Line(self.ax.c2p(self.t0 + self.dt, .5*self.y0), self.ax.c2p(self.t0 + self.dt, self.y0)),
            direction=RIGHT, color=BLACK, fill_opacity=.5
        )
        brace_tex = MathTex(r"\Delta f = \frac{1}{2}", color=BLACK).scale(.8).set_opacity(.5)
        brace_tex.next_to(brace, RIGHT)
        self.add(brace, brace_tex)
