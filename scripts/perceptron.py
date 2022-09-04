from manim import *
from numpy import *


class Perceptron(Scene):
    def construct(self):
        ax = Axes(x_range=[-3.5, 3.5], y_range=[-3.5, 3.5], x_length=7).add_coordinates()
        dot1 = Dot(ax.c2p(0, 0), color=RED_A)
        dot2 = Dot(ax.c2p(0, 1), color=BLUE_A)
        dot3 = Dot(ax.c2p(1, 0), color=BLUE_A)
        dot4 = Dot(ax.c2p(1, 1), color=BLUE_A)
        dots = Group(dot1, dot2, dot3, dot4)

        perceptron_graph = ax.plot(lambda x: -x + 0.5, color=ORANGE)
        self.add(ax, dots, perceptron_graph)

        pass
