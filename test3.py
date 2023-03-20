import math


def xrange(n):
    x = 0
    while x != n:
        yield x
        x += 1


# for n in xrange(10):
#     print(n)

def distance(point1, point2):
    x = point1[0] - point2[0]
    y = point1[1] - point2[1]
    print("x:", x, "y:", y)
    dis = math.sqrt(x*x + y*y)
    return dis


result = distance((0, 0), (3, 4))
print(result)
