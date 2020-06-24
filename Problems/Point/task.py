class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, second_point):
        return ((self.x - second_point.x) ** 2 + (self.y - second_point.y) ** 2) ** (1 / 2)