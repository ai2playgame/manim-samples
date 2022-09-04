from manim import *
from numpy import *


class Sekibun(Scene):
    def construct(self):
        axes = Axes(x_range=[-4, 4], y_range=[-2, 2, 0.2],
                    x_axis_config={'numbers_to_include': [-2, 3]})

        def graph1_func(x):
            return np.cos(x)

        graph1 = axes.plot(graph1_func, x_range=[-4, 4], color=BLUE_C)
        graph1_label = axes.get_graph_label(
            graph1, 'sin(x)', x_val=1.0, direction=UR, color=BLUE_C)

        area = axes.get_area(graph1, [-2, 3], color=GREY, opacity=0.5)

        self.add(axes, graph1, graph1_label, area)
