class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = (1 / 2) * self.a * self.b



# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
triangle = RightTriangle(input_c, input_a, input_b)
if triangle.c ** 2 == (triangle.a ** 2 + triangle.b ** 2):
    print(triangle.area)
else:
    print("Not right")
