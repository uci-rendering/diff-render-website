from manim import *
from manim.utils.color import Colors
import numpy as np

config.background_color = WHITE
point_color = GRAY # Colors.light_gray.value

_A = np.array([2.5, 1., 0.])
offset = np.array([2., 2., 0.])

def coord_to_str(coord):
    return "(%.1f, %.1f)" % (coord[0], coord[1])


def init_numberplane(x_range, y_range, length=1., precision=0):
    numberplane = NumberPlane(
        x_range = x_range,
        y_range = y_range,

        axis_config = {
            "color": Colors.light_gray.value,
            "stroke_width": 2,
            "include_numbers": True,
            "include_ticks": True,
            "decimal_number_config": {
                "num_decimal_places": precision,
                "color": Colors.light_gray.value,
            },
            "unit_size": length
        },

        # x_axis_config = {
        #     "label_direction": RIGHT + DOWN
        # },

        y_axis_config = {
            "label_direction": LEFT + DOWN
        },

        background_line_style = {
            "stroke_color": Colors.lighter_gray.value,
            "stroke_opacity": 0.4,
            "stroke_width": 1
        }
    )
    return numberplane, numberplane.get_origin()


def init_vg_dot(name, pos, orig, dir1, dir2):
    dot = Dot(pos, color=point_color)
    vg = init_vg_vec2((pos - orig)[0:2]).next_to(pos, dir1)
    label = MathTex("\\boldsymbol{%s}" % name, color=point_color).scale(.8).next_to(pos, dir2)
    return dot, vg, label


def init_vg_vec2(vec):
    assert len(vec) == 2

    vg = VGroup(Text("(", color=point_color))
    vg.add(DecimalNumber(vec[0], color=point_color).next_to(vg[0], buff=0.1))
    vg.add(Text(", ", color=point_color).next_to(vg[0], buff=1.1))
    vg.add(DecimalNumber(vec[1], color=point_color).next_to(vg[0], buff=1.4))
    vg.add(Text(")", color=point_color).next_to(vg[0], buff=2.3))
    return vg.scale(.8).set_opacity(.4)


class PointDefinition(Scene):
    def construct(self):
        self.numberplane, self.origin = init_numberplane((-1, 13, 1), (-1, 7, 1))
        self.add(self.numberplane)

        self.A = self.origin + _A
        self.B = self.A + offset

        self.dot_A, self.vg_A, self.label_A = init_vg_dot("A", self.A, self.origin, LEFT, DOWN)
        self.dot_B, self.vg_B, self.label_B = init_vg_dot("B", self.B, self.origin, RIGHT, UP)

        self.add(self.dot_A, self.vg_A, self.label_A, self.dot_B, self.vg_B, self.label_B)


class VectorDefinition1(PointDefinition):
    def construct(self):
        super().construct()

        self.C = .5*(self.A + self.B)
        self.D = self.A + np.array([offset[0], 0., 0.])

        self.arrow = Arrow(start=self.A, end=self.B, color=ORANGE, buff=0.)
        self.arrow_label = MathTex(r"\boldsymbol{a}", color=ORANGE).scale(1.2)
        self.arrow_label.next_to(self.arrow, np.array([-1., 1., 0]), buff=-0.85)

        self.add(self.arrow, self.arrow_label)


class VectorDefinition2(VectorDefinition1):
    def construct(self, animate=True):
        super().construct()

        self.vg_dash = VGroup()
        self.vg_dash.add(DashedLine(start=self.A, end=self.D, color=ORANGE, buff=0.))
        self.vg_dash.add(DecimalNumber(2., color=ORANGE).scale(.8).next_to(self.vg_dash[0], DOWN))
        self.vg_dash.add(DashedLine(start=self.B, end=self.D, color=ORANGE, buff=0.))
        self.vg_dash.add(DecimalNumber(2., color=ORANGE).scale(.8).next_to(self.vg_dash[2], RIGHT))
        self.vg_dash.set_opacity(.4)

        self.main_label = MathTex(
            r"\boldsymbol{a} = \overrightarrow{\boldsymbol{AB}} := \boldsymbol{B} - \boldsymbol{A} = (2.00, 2.00)",
            color=ORANGE
        )
        # self.main_label[0][5:7].set_color(point_color)
        self.main_label[0][9:12:2].set_color(point_color)
        self.main_label.move_to(self.origin + np.array([6., -.65, 0.]))

        self.add(self.vg_dash, self.main_label)


class VectorTranslation(VectorDefinition2):
    def construct(self):
        super().construct(False)

        def update_vg_A(obj):
            obj.next_to(self.arrow.get_start_and_end()[0], LEFT)
            obj[1].set_value(self.arrow.get_start_and_end()[0][0] - self.origin[0])
            obj[3].set_value(self.arrow.get_start_and_end()[0][1] - self.origin[1])
        self.vg_A.add_updater(update_vg_A)
        self.dot_A.add_updater(lambda x: x.move_to(self.arrow.get_start_and_end()[0]))
        self.label_A.add_updater(lambda x: x.next_to(self.arrow.get_start_and_end()[0], DOWN))

        def update_vg_B(obj):
            obj.next_to(self.arrow.get_start_and_end()[1], RIGHT)
            obj[1].set_value(self.arrow.get_start_and_end()[1][0] - self.origin[0])
            obj[3].set_value(self.arrow.get_start_and_end()[1][1] - self.origin[1])
        self.vg_B.add_updater(update_vg_B)
        self.dot_B.add_updater(lambda x: x.move_to(self.arrow.get_start_and_end()[1]))
        self.label_B.add_updater(lambda x: x.next_to(self.arrow.get_start_and_end()[1], UP))

        def update_vg_dash(obj):
            obj[0].move_to(self.arrow.get_center() - np.array([0., .5*offset[1], 0.]))
            obj[1].next_to(obj[0], DOWN)
            obj[2].move_to(self.arrow.get_center() + np.array([.5*offset[0], 0., 0.]))
            obj[3].next_to(obj[2], RIGHT)
        self.vg_dash.add_updater(update_vg_dash)

        self.arrow_label.add_updater(lambda x: x.next_to(self.arrow, np.array([-1., 1., 0]), buff=-0.85))

        C2 = self.C + np.array([5.5, 0., 0.])
        curve = CubicBezier(self.C, self.C + np.array([1., 3., 0.]), C2 + np.array([-1., 3., 0.]), C2)
        self.play(MoveAlongPath(self.arrow, curve), run_time=2.5, rate_func=linear)


class VectorNormalize1(Scene):
    def construct(self, show_length=True):
        self.unit = 2.
        self.numberplane, self.origin = init_numberplane((-.5, 6.5, .5), (-.5, 3.5, .5), self.unit, 1)
        self.add(self.numberplane)

        self.vec = np.array([4., 3., 0.])
        self.vec_len = np.linalg.norm(self.vec)

        self.v = Arrow(start=self.origin, end=self.origin + self.vec*self.unit, color=ORANGE, buff=0.)

        if show_length:
            self.v_label = MathTex(r"\boldsymbol{a} = (4, 3)", color=ORANGE).scale(1.2)
            self.v_label.move_to(self.v.get_center() + RIGHT*1.5 + DOWN*.3)
        else:
            self.v_label = MathTex(r"\boldsymbol{a}", color=ORANGE).scale(1.2)
            self.v_label.move_to(self.v.get_center() + RIGHT*.5 + DOWN*.3)

        self.add(self.v, self.v_label)

        if show_length:
            self.v_brace = Brace(self.v, direction=self.v.copy().rotate(PI / 2).get_unit_vector(), color=GRAY)
            self.v_brace_txt = self.v_brace.get_tex(r"\| \boldsymbol{a} \| = 5").set_color(GRAY).scale(1.2)

            self.add(self.v_brace, self.v_brace_txt)


class VectorNormalize2(VectorNormalize1):
    def construct(self):
        super().construct()

        self.vh = Arrow(start=self.origin, end=self.origin + self.vec*(self.unit/self.vec_len), color=GREEN, buff=0.)
        self.vh_label = MathTex(r"\hat{\boldsymbol{a}} := \boldsymbol{a}/\| \boldsymbol{a} \| = (0.8, 0.6)", color=GREEN)
        self.vh_label.move_to(self.vh.get_center() + RIGHT*3. + DOWN*.1)
        self.add(self.vh, self.vh_label)


class VectorAddition1(Scene):
    def construct(self, add=True):
        self.unit = 2.
        self.opaticy = .5

        self.numberplane, self.origin = init_numberplane((-.5, 6.5, .5), (-.5, 3.5, .5), self.unit, 1)
        self.add(self.numberplane)

        self.vec1 = np.array([3., 1., 0.])
        self.vec2 = np.array([1., 2., 0.])

        self.v1 = Arrow(start=self.origin, end=self.origin + self.vec1*self.unit, color=ORANGE, buff=0.).set_opacity(self.opaticy)
        self.v1_label = MathTex(r"\boldsymbol{a}", color=ORANGE).set_opacity(self.opaticy).scale(1.2)
        self.v1_label.move_to(self.v1.get_center() + RIGHT*.5 + DOWN*.3)

        self.v2 = Arrow(start=self.origin, end=self.origin + self.vec2*self.unit, color=ORANGE, buff=0.).set_opacity(self.opaticy)
        self.v2_label = MathTex(r"\boldsymbol{b}", color=ORANGE).set_opacity(self.opaticy).scale(1.2)
        self.v2_label.move_to(self.v2.get_center() + RIGHT*.4 + DOWN*.2)

        if add:
            self.add(self.v1, self.v1_label, self.v2, self.v2_label)


class VectorAddition2(VectorAddition1):
    def construct(self):
        super().construct()

        src = self.v2.get_center()
        delta = self.v1.get_vector()

        self.v2_label.add_updater(lambda x: x.move_to(self.v2.get_center() + RIGHT*.4 + DOWN*.2))
        self.play(MoveAlongPath(self.v2, Line(start=src, end=src + delta)), run_time=1., rate_func=linear)
        self.wait(.5)

        self.v3 = Arrow(start=self.v1.get_start_and_end()[0], end=self.v2.get_start_and_end()[1], color=ORANGE, buff=0.)
        self.v3_label = MathTex(r"\boldsymbol{a} + \boldsymbol{b}", color=ORANGE).scale(1.2)
        self.v3_label.move_to(self.v3.get_center() + LEFT + UP *.2)
        self.play(FadeIn(self.v3), FadeIn(self.v3_label), run_time=.5)


class VectorCartesian1(VectorNormalize1):
    def construct(self):
        super().construct(False)

class VectorCartesian2(VectorCartesian1):
    def construct(self, add=True):
        super().construct()

        vX = Arrow(start=self.origin, end=self.origin + np.array([1., 0., 0.])*self.unit, color=GREEN, buff=0.)
        vX_label = MathTex(r"\hat{\boldsymbol{X}}", color=GREEN).move_to(vX.get_center() + DOWN*.6)
        self.vg_X = VGroup(vX, vX_label)

        vY = Arrow(start=self.origin, end=self.origin + np.array([0., 1., 0.])*self.unit, color=GREEN, buff=0.)
        vY_label = MathTex(r"\hat{\boldsymbol{Y}}", color=GREEN).move_to(vY.get_center() + LEFT*.6)
        self.vg_Y = VGroup(vY, vY_label)

        if add:
            self.add(self.vg_X, self.vg_Y)

class VectorCartesian3(VectorCartesian2):
    def construct(self, animate=True):
        super().construct(False)

        self.opaticy = .4

        vXs = Arrow(start=self.origin, end=self.origin + np.array([1., 0., 0.])*self.unit*self.vec[0], color=ORANGE, buff=0.).set_opacity(self.opaticy)
        vXs_label = MathTex("%.0f" % self.vec[0], r"\hat{\boldsymbol{X}}", color=ORANGE)
        vXs_label[1][:].set_color(GREEN)
        vXs_label.set_opacity(self.opaticy).move_to(vXs.get_center() + DOWN*.6)
        self.vg_Xs = VGroup(vXs, vXs_label)

        vYs = Arrow(start=self.origin, end=self.origin + np.array([0., 1., 0.])*self.unit*self.vec[1], color=ORANGE, buff=0.).set_opacity(self.opaticy)
        vYs_label = MathTex("%.0f" % self.vec[1], r"\hat{\boldsymbol{Y}}", color=ORANGE)
        vYs_label[1][:].set_color(GREEN)
        vYs_label.set_opacity(self.opaticy).move_to(vYs.get_center() + LEFT*.6)
        self.vg_Ys = VGroup(vYs, vYs_label)

        self.dashed1 = DashedLine(start=self.v.get_start_and_end()[1], end=self.v.get_start_and_end()[1] + DOWN*self.vec[1]*self.unit, color=ORANGE).set_opacity(self.opaticy)
        self.dashed2 = DashedLine(start=self.v.get_start_and_end()[1], end=self.v.get_start_and_end()[1] + LEFT*self.vec[0]*self.unit, color=ORANGE).set_opacity(self.opaticy)

        self.eqn = MathTex("= ", "4", r"\hat{\boldsymbol{X}}", " + ", "3", r"\hat{\boldsymbol{Y}}", color=ORANGE)
        self.eqn[2][:].set_color(GREEN)
        self.eqn[5][:].set_color(GREEN)
        self.eqn.move_to(self.v_label.get_center() + RIGHT*1.65 + UP*.07)

        self.add(self.vg_Xs, self.vg_Ys, self.dashed1, self.dashed2, self.eqn)
        self.add(self.vg_X, self.vg_Y)

        if animate:
            eqn2 = MathTex("= ", r"\begin{pmatrix} 4\\ 3 \end{pmatrix}", color=ORANGE).move_to(self.v_label.get_center() + RIGHT*1.06 + DOWN*0.02)
            self.play(Transform(self.eqn, eqn2), run_time=1.)
            # self.add(eqn2)


class VectorChangeBasis(VectorCartesian3):
    def construct(self):
        super().construct(False)

        vY1 = Arrow(start=self.origin, end=self.origin + np.array([0., 1., 0.])*self.unit, color=PURPLE, buff=0.)
        vY1_label = MathTex(r"\tilde{\boldsymbol{Y}}", color=PURPLE).move_to(vY1.get_center() + LEFT*.6)
        vg_Y1 = VGroup(vY1, vY1_label)

        vYs1_label = MathTex("3", r"\tilde{\boldsymbol{Y}}", color=ORANGE)
        vYs1_label[1][:].set_color(PURPLE)
        vYs1_label.set_opacity(self.opaticy).move_to(self.vg_Ys[0].get_center() + LEFT*.6)

        self.add(self.vg_Y.copy().set_opacity(self.opaticy))
        self.play(AnimationGroup(Transform(self.vg_Ys[1], vYs1_label), Transform(self.vg_Y, vg_Y1)), run_time=.5)

        def trans_fun(p):
            return p + RIGHT*(p[1] - self.origin[1])*.5

        self.numberplane.prepare_for_nonlinear_transform()
        lst_objs = [self.numberplane, self.vg_Ys, self.vg_Y]
        lst_ani = [o.animate.apply_function(trans_fun) for o in lst_objs]

        vXs1 = Arrow(start=self.origin, end=self.origin + np.array([1., 0., 0.])*self.unit*2.5, color=ORANGE, buff=0.).set_opacity(self.opaticy)
        vXs1_label = MathTex("2.5", r"\hat{\boldsymbol{X}}", color=ORANGE)
        vXs1_label[1][:].set_color(GREEN)
        vXs1_label.set_opacity(self.opaticy).move_to(vXs1.get_center() + DOWN*.6)
        vg_Xs1 = VGroup(vXs1, vXs1_label)
        lst_ani.append(Transform(self.vg_Xs, vg_Xs1))

        # Making sure self.vg_X stays on top of self.vg_Xs
        lst_ani.append(Transform(self.vg_X, self.vg_X))

        dashed1_new = DashedLine(start=self.dashed1.get_start_and_end()[0], end=self.dashed1.get_start_and_end()[1] + LEFT*self.unit*1.5, color=ORANGE).set_opacity(self.opaticy)
        lst_ani.append(Transform(self.dashed1, dashed1_new))

        dashed2_new = DashedLine(start=self.dashed2.get_start_and_end()[0], end=self.dashed2.get_start_and_end()[1] + RIGHT*self.unit*1.5, color=ORANGE).set_opacity(self.opaticy)
        lst_ani.append(Transform(self.dashed2, dashed2_new))

        eqn2 = MathTex("= ", "2.5", r"\hat{\boldsymbol{X}}", " + ", "3", r"\tilde{\boldsymbol{Y}}", color=ORANGE)
        eqn2[2][:].set_color(GREEN)
        eqn2[5][:].set_color(PURPLE)
        eqn2.move_to(self.v_label.get_center() + RIGHT*1.85 + UP*.07)
        lst_ani.append(Transform(self.eqn, eqn2))

        self.play(AnimationGroup(*lst_ani), run_time=2.)
        self.wait(1.)

        eqn3 = MathTex("= ", r"\begin{pmatrix} 2.5\\ 3 \end{pmatrix}", color=ORANGE).move_to(self.v_label.get_center() + RIGHT*1.28 + DOWN*0.02)
        self.play(Transform(self.eqn, eqn3), run_time=1.)


class VectorDotProduct1(VectorAddition1):
    def construct(self, add=True):
        super().construct(add)

        self.v1.set_opacity(1.)
        self.v1_label.set_opacity(1.)
        self.v2.set_opacity(1.)
        self.v2_label.set_opacity(1.)
        v2_copy = self.v2.copy()

        self.theta_arc = Angle(self.v1, self.v2, color=BLACK, radius=1., other_angle=False)

        self.theta_label = MathTex(r"\theta", color=BLACK).scale(1.2).move_to(
            Angle(self.v1, v2_copy, radius=1. + SMALL_BUFF*4, other_angle=False).point_from_proportion(0.5)
        )

        self.remove(self.numberplane)
        if add:
            self.add(self.theta_arc, self.theta_label)


class VectorDotProduct2(VectorDotProduct1):
    def construct(self):
        super().construct(False)

        v1p = Arrow(start=self.v1.get_start_and_end()[0], end=self.v1.get_projection(self.v2.get_start_and_end()[1]), color=PURPLE, buff=0.)
        v1p_dashed = DashedLine(start=self.v2.get_start_and_end()[1], end=v1p.get_start_and_end()[1], color=PURPLE, buff=0.).set_opacity(self.opaticy)
        v1p_angle = RightAngle(v1p, v1p_dashed, color=Colors.lighter_gray.value, length=.5, quadrant=(1,-1))
        v1p_label = MathTex(r"\boldsymbol{b}_{\bot}", color=PURPLE).scale(1.2).move_to(v1p.get_center() + RIGHT*.3 + DOWN*.5)
        self.vg_v1p = VGroup(v1p, v1p_dashed, v1p_angle, v1p_label)

        self.v1p_tri = Polygon(*v1p.get_start_and_end(), v1p_dashed.get_start_and_end()[0], fill_opacity=.5, color=Colors.lighter_gray.value)

        self.add(self.v1p_tri)
        self.add(self.v1, self.v1_label, self.v2, self.v2_label, self.theta_arc, self.theta_label)
        self.add(self.vg_v1p)


class VectorDotProduct3(VectorDotProduct2):
    def construct(self):
        super().construct()

        tri_copy = VGroup(self.v1p_tri.copy(), self.theta_arc.copy(), self.theta_label.copy())

        self.play(MoveAlongPath(tri_copy, Line(start=tri_copy.get_center(), end=tri_copy.get_center() + RIGHT*8.)))

        vtx = tri_copy[0].get_vertices()

        lst_l = [Line(start=vtx[1], end=vtx[0]), Line(start=vtx[0], end=vtx[2])]
        lst_b = [Brace(l, direction=l.copy().rotate(PI/2.).get_unit_vector(), color=GRAY) for l in lst_l]
        lst_t = [lst_b[0].get_tex(r"\| \boldsymbol{b}_{\bot} \|"), lst_b[1].get_tex(r"\| \boldsymbol{b} \|")]

        self.play(AnimationGroup(*([FadeIn(b) for b in lst_b] + [FadeIn(t.set_color(GRAY)) for t in lst_t])))


class VectorCrossProduct(ThreeDScene):
    def construct(self):
        ax = ThreeDAxes(
            axis_config = {
                "color": Colors.light_gray.value,
                # "stroke_width": 2,
                # "include_numbers": False,
                "include_ticks": False,
            },
        )

        vec1 = np.array([2., 0., 0.])
        vec2 = np.array([0., 1., 0.])
        vec3 = np.cross(vec1, vec2)
        margin = .3;

        obj_s = Surface(
            lambda u, v: vec1*u + vec2*v,
            u_range=[0., 1.], v_range=[0., 1.],
            resolution=1, fill_opacity=0.3, checkerboard_colors=[PURPLE]
        )

        self.set_camera_orientation(phi=75.*DEGREES, theta=45.*DEGREES, zoom=1.2)
        self.add(ax, obj_s)

        # obj_sl = MathTex(r"\| \boldsymbol{a} \times \boldsymbol{b} \|", color=PURPLE).move_to(.5*(vec1 + vec2))
        # self.add_fixed_orientation_mobjects(obj_sl)

        obj_v = [Arrow3D(start=np.array([0., 0., 0.]), end=v, color=ORANGE, resolution=8) for v in [vec1, vec2, vec3]]
        obj_v[-1].set_color(PURPLE)

        obj_l = [
            MathTex(r"\boldsymbol{a}", color=ORANGE).move_to(vec1 + vec1/np.linalg.norm(vec1)*margin),
            MathTex(r"\boldsymbol{b}", color=ORANGE).move_to(vec2 + vec2/np.linalg.norm(vec2)*margin),
            MathTex(r"\boldsymbol{a} \times \boldsymbol{b}", color=PURPLE).move_to(vec3 + vec3/np.linalg.norm(vec3)*margin)
        ]

        self.add(*obj_v)
        self.add_fixed_orientation_mobjects(*obj_l)

        a = Dot(vec1).set_opacity(0.)
        b = Dot(vec2).set_opacity(0.)

        obj_v[0].add_updater(
            lambda x: x.become(Arrow3D(start=np.array([0., 0., 0.]), end=a.get_center(), color=ORANGE, resolution=8))
        )

        obj_l[0].add_updater(
            lambda x: x.move_to(a.get_center() + a.get_center()/np.linalg.norm(a.get_center())*margin)
        )

        obj_v[1].add_updater(
            lambda x: x.become(Arrow3D(start=np.array([0., 0., 0.]), end=b.get_center(), color=ORANGE, resolution=8))
        )

        obj_l[1].add_updater(
            lambda x: x.move_to(b.get_center() + b.get_center()/np.linalg.norm(b.get_center())*margin)
        )

        def v3_update(o):
            vv = np.cross(a.get_center(), b.get_center())
            o.become(Arrow3D(start=np.array([0., 0., 0.]), end=vv, color=PURPLE, resolution=8))

        def l3_update(o):
            vv = np.cross(a.get_center(), b.get_center())
            o.move_to(vv + vv/np.linalg.norm(vv)*margin)

        obj_v[2].add_updater(v3_update)
        obj_l[2].add_updater(l3_update)

        def s_update(o):
            o.become(
                Surface(
                    lambda u, v: a.get_center()*u + b.get_center()*v,
                    u_range=[0., 1.], v_range=[0., 1.],
                    resolution=1, fill_opacity=0.3, checkerboard_colors=[PURPLE]
                )
            )
        obj_s.add_updater(s_update)

        # obj_sl.add_updater(lambda x: x.move_to(.5*(a.get_center() + b.get_center())))

        self.play(MoveAlongPath(a, Line(start=vec1, end=vec1 + np.array([0., 0., -1.25]))), run_time=1.)
        self.wait(.5)
        self.play(MoveAlongPath(b, Line(start=vec2, end=vec2 + np.array([0., .5, 0.]))), run_time=1.)


class VectorCrossProduct2(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75.*DEGREES, theta=45.*DEGREES, zoom=1.2)

        A = np.array([3., 0., 0.])
        B = np.array([0., 2., 0.])
        C = np.array([-1., -2., 0.])

        n = np.cross(B - A, C - A)
        n /= np.linalg.norm(n)

        def fun_tri(u, v):
            ratio = np.linalg.norm(np.array([u/(u + v), v/(u + v)]))/np.sqrt(1. + min(u, v)**2.) if u + v > 0. else 0.
            return A + (B - A)*u*ratio + (C - A)*v*ratio

        obj_s = Surface(fun_tri, resolution=1, fill_opacity=.3, checkerboard_colors=[PURPLE])

        AB_v = Arrow3D(start=A, end=B, color=ORANGE, resolution=8)
        AC_v = Arrow3D(start=A, end=C, color=ORANGE, resolution=8)
        n_v = Arrow3D(start=A, end=A + n, color=PURPLE, resolution=8)

        A_l = MathTex(r"A", color=GRAY).move_to(np.array([3.25, 0., 0.]))
        B_l = MathTex(r"B", color=GRAY).move_to(np.array([0., 2.25, 0.]))
        C_l = MathTex(r"C", color=GRAY).move_to(np.array([-1.7, -2.7, 0.05]))
        n_l = MathTex(r"\frac{\overrightarrow{AB} \times \overrightarrow{AC}}{\| \overrightarrow{AB} \times \overrightarrow{AC} \|}", color=PURPLE).scale(.8).move_to(A + n + np.array([.2, 0., .45]))

        self.add(obj_s, AB_v, AC_v, n_v)
        self.add_fixed_orientation_mobjects(A_l, B_l, C_l, n_l)


def get_matrix(arr, clr=BLACK, scl=1.):
    return Matrix(arr, element_alignment_corner=UL, left_bracket="(", right_bracket=")").set_color(clr).scale(scl)


def get_dot_eqn(a, b, fmt="%d", clr=BLACK, scl=1.):
    assert len(a) == len(b)
    m = len(a)
    s = " = " + (fmt % a[0]) + r" \times " + (fmt % b[0])
    for i in range(1, m):
        s = s + " + " + (fmt % a[i]) + r" \times " + (fmt % b[i])
    s = s + " = " + (fmt % np.dot(a, b))
    return MathTex(s, color=clr).scale(scl)


def process_row_column(mat_a, mat_b, i, j, v_mat_a=None, v_mat_b=None, v_mat_ab=None, color=BLACK, scale=1.):
    assert np.size(mat_a, 1) == np.size(mat_b, 0)

    if v_mat_a:
        v_mat_a.add(SurroundingRectangle(v_mat_a.get_rows()[i], stroke_opacity=0., fill_color=color, fill_opacity=.2))
    if v_mat_b:
        v_mat_b.add(SurroundingRectangle(v_mat_b.get_columns()[j], stroke_opacity=0., fill_color=color, fill_opacity=.2))
    if v_mat_ab:
        v_mat_ab.add(SurroundingRectangle(v_mat_ab.get_entries()[i*np.size(mat_b, 1) + j], stroke_opacity=0., fill_color=color, fill_opacity=.2))

    return VGroup(
        get_matrix(mat_a[[i],:], clr=color, scl=scale),
        get_matrix(mat_b[:,[j]], clr=color, scl=scale),
        get_dot_eqn(mat_a[i, :], mat_b[:, j], clr=color, scl=scale)
    ).arrange_in_grid(rows=1)


class MatrixMult0(Scene):
    def construct(self, add=True):
        self.mat_a = np.array([[1, 3], [5, 2], [0, 4]])
        self.mat_b = np.array([[3, 6, 9, 4], [2, 7, 8, 3]])
        self.mat_c = np.dot(self.mat_a, self.mat_b)

        A = get_matrix(self.mat_a, scl=.9)
        B = get_matrix(self.mat_b, scl=.9)
        C = get_matrix(self.mat_c, scl=.9)

        self.gp = VGroup(A, MathTex(r"\times", color=BLACK), B, MathTex("=", color=BLACK), C).arrange_in_grid(rows=1)
        if add:
            self.add(self.gp)

class MatrixMult1(MatrixMult0):
    def construct(self):
        super().construct(add=False)

        gp1 = process_row_column(self.mat_a, self.mat_b, 0, 1, v_mat_a=self.gp[0], v_mat_b=self.gp[2], v_mat_ab=self.gp[4], color=RED)
        self.add(self.gp, gp1.scale(.8).next_to(self.gp, DOWN))

class MatrixMult2(MatrixMult0):
    def construct(self):
        super().construct(add=False)

        gp2 = process_row_column(self.mat_a, self.mat_b, 2, 3, v_mat_a=self.gp[0], v_mat_b=self.gp[2], v_mat_ab=self.gp[4], color=GREEN)
        self.add(self.gp, gp2.scale(.8).next_to(self.gp, DOWN))
