class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x, y):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "Point x: " + str(self.y) + "\n" + "Point y: " + str(self.x) + "\n"
class Rectangle:
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "postion: " + "\n" + str(self.corner) + "\n" + "width: " + str(self.width) + "\n" + "height: " + str(self.height)


r = Rectangle(Point(4, 5), 6, 5)

print(r)
