import math


class circle():
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


# take two cirlce
def intersected_area(c1, c2):
    d = math.sqrt((c1.x-c2.x)*(c1.x-c2.x) + (c1.y-c2.y)*(c1.y-c2.y))
    if (d >= c1.radius + c2.radius):
        return
    if (c1.radius > c2.radius):
        tmp = c1.radius
        c1.radius = c2.radius
        c2.radius = tmp
    if (c2.radius - c1.radius >= d):
        return math.pi * c1.radius * c1.radius

    ang1 = math.acos((c1.radius * c1.radius + d * d -
                     c2.radius * c2.radius) / (2 * c1.radius * d))
    ang2 = math.acos((c2.radius * c2.radius + d * d -
                     c1.radius * c1.radius) / (2 * c2.radius * d))
    return ((ang1 * c1.radius * c1.radius) + (ang2 * c2.radius * c2.radius) - (c1.radius * d * math.sin(ang1)))


def main():
    c1 = circle(2, 2, 5)
    c2 = circle(7, 2, 5)
    result = intersected_area(c1, c2)
    print("intersected_area: ", result)


if __name__ == "__main__":
    main()
