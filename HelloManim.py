from manim import *
from numpy import *


class GraphArea(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-2, 6],
            y_range=[-2, 2, 0.2],
            axis_config={"include_numbers": False, "include_tip": False}
        )

        def curve_1_func(x):
            return np.sin(x)
        curve_1 = ax.plot(curve_1_func,
                          x_range=[-2, 6], color=BLUE_C)
        label_1 = ax.get_graph_label(curve_1, 'sin(x)', x_val=2, direction=UR)

        x = ValueTracker(1)
        secant = always_redraw(
            lambda: ax.get_secant_slope_group(
                x=x.get_value(),
                graph=curve_1,
                dx=0.0001,
                secant_line_length=6,
                secant_line_color=RED_D,
            )
        )
        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(ax.c2p(x.get_value(), curve_1_func(x.get_value())))
        )

        self.add(ax, curve_1, label_1, secant, dot1)
        self.wait()
        self.play(x.animate.set_value(-1), run_time=2)
        self.wait(1)
        self.play(x.animate.set_value(5), run_time=6)
