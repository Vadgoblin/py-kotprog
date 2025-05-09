def is_point_in_trapezoid(trapezoid, point):
    """
    Determines if a point is inside a trapezoid.

    :param trapezoid: List of 4 tuples (x, y) representing the vertices
        of the trapezoid.
    :param point: A tuple (x, y) representing the point.
    :return: True if the point is inside the trapezoid, False otherwise.
    """
    x, y = point
    count = 0
    n = len(trapezoid)

    for i in range(n):
        x1, y1 = trapezoid[i]
        x2, y2 = trapezoid[(i + 1) % n]

        # Check if point is on an edge (optional, for exact boundary detection)
        if ((y - y1) * (x2 - x1) == (x - x1) * (y2 - y1) and
                min(x1, x2) <= x <= max(x1, x2) and
                min(y1, y2) <= y <= max(y1, y2)):
            return True

        # Count intersections with a horizontal ray to the right
        if (y1 > y) != (y2 > y):
            xinters = (x2 - x1) * (y - y1) / (y2 - y1 + 1e-10) + x1
            if x < xinters:
                count += 1

    return count % 2 == 1
