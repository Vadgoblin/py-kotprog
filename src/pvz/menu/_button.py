from .is_point_in_trapezoid import is_point_in_trapezoid


class Button:
    def __init__(self, edges: "tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]"):
        self._edges = edges

    def is_clicked(self, click_pos):
        return is_point_in_trapezoid(self._edges, click_pos)
