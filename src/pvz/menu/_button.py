from .is_point_in_trapezoid import is_point_in_trapezoid


class Button:
    """
    Represents a button defined by a trapezoid.

    The button is considered clicked if a given point lies within its trapezoidal bounds.
    """

    def __init__(

            self,
            edges: "tuple[tuple[int, int], tuple[int, int], tuple[int, int], tuple[int, int]]"
    ):
        """
        Initialize the button with its trapezoidal edges.

        Args:
            edges: A tuple of four (x, y) points defining the trapezoid.
        """

        self._edges = edges

    def is_clicked(self, click_pos):
        """
        Determine whether a click position falls inside the trapezoidal button.

        Args:
            click_pos: The (x, y) coordinates of the click.

        Returns:
            True if the click is within the trapezoid, False otherwise.
        """
        return is_point_in_trapezoid(self._edges, click_pos)
