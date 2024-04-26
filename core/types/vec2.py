
class Vec2(tuple):
    def __init__(self, x, y):
        super.__init__(x, y)

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]