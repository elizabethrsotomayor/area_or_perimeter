def area_or_perimeter(l: int, w: int) -> int:
    """
    Given the length and width of a 4-sided polygon, return the area if it is a square and the
    perimeter if it is a rectangle.
    :param l: int value representing the length of a polygon
    :param w: int value representing width of polygon
    :return:
    """
    if l == w:
        return l*w
    else:
        return (l*2) + (w*2)
