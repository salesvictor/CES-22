class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """

        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """

        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """

        self.corner.x += dx
        self.corner.y += dy

    def contains(self, p):
        return self.corner.x <= p.x <= self.corner.x + self.w and self.corner.y <= p.y <= self.corner.y + self.h


def move_point(p, x, y):
    return Point(p.x + x, p.y + y)


def collide(rect1, rect2):
    a1 = move_point(rect1.corner, 0, 0)  # rect1 upper-left corner
    a2 = move_point(rect1.corner, rect1.w, 0)  # rect1 upper-right corner
    a3 = move_point(rect1.corner, 0, rect1.h)  # rect1 lower-left corner
    a4 = move_point(rect1.corner, rect1.w, rect1.h)  # rect1 lower-right corner

    b1 = move_point(rect2.corner, 0, 0)  # rect2 upper-left corner
    b2 = move_point(rect2.corner, rect2.w, 0)  # rect2 upper-right corner
    b3 = move_point(rect2.corner, 0, rect2.h)  # rect2 lower-left corner
    b4 = move_point(rect2.corner, rect2.w, rect2.h)  # rect2 lower-right corner

    # check if any of rect2 corners is inside rect1
    if rect1.contains(b1) or rect1.contains(b2) or rect1.contains(b3) or rect1.contains(b4):
        return True

    # check if any of rect1 corners is inside rect2
    if rect2.contains(a1) or rect2.contains(a2) or rect2.contains(a3) or rect2.contains(a4):
        return True

    return False
