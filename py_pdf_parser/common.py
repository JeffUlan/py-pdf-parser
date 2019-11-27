class BoundingBox:
    """
    A rectangle, stored using the coordinates (x0, y0) of the bottom left corner, and
    the coordinates (x1, y1) of the top right corner.

    Args:
        x0 (int): The x coordinate of the bottom left corner.
        x1 (int): The x coordinate of the top right corner.
        y0 (int): The y coordinate of the bottom left corner.
        y1 (int): The y coordinate of the top right corner.

    Attributes:
        x0 (int): The x coordinate of the bottom left corner.
        x1 (int): The x coordinate of the top right corner.
        y0 (int): The y coordinate of the bottom left corner.
        y1 (int): The y coordinate of the top right corner.
        width (int): The width of the box, equal to x1 - x0.
        height (int): The height of the box, equal to y1 - y0.
    """

    def __init__(self, x0, x1, y0, y1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.width = x1 - x0
        self.height = y1 - y0