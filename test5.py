# points = [(1, 2), (3, 4), (5, 6)]
# parent_points = [points]


# xsum = 0
# ysum = 0

# for i in points:
#     xsum += i[0]
#     ysum += i[1]

# print("xsum: ", xsum, "\n", "ysum: ", ysum)

# avg_point = (xsum/len(points), ysum/len(points))

# print("center_point: ", avg_point)

# for i in parent_points:
#     print(i[0])


class Node:
    def __init__(self, centroid):
        self.centroid = centroid
        self.point = []
        self.child = []


p1 = Node((1, 2))
p2 = Node((3, 4))
p3 = Node((5, 6))

pp1 = Node((7, 8))
pp2 = Node((9, 10))
pp3 = Node((11, 12))

r = Node((66, 66))

root = Node((0, 0))
root.point.append(r)
root.child.append(p1)
root.child.append(p2)
root.child.append(p3)

p1.point.append(pp1)
p1.point.append(pp2)
p3.point.append(pp3)


def print_all(x):
    for i in x.point:
        print(i.centroid)

    if len(x.child) > 0:
        print("have child")
        for i in x.child:
            print_all(i)    # 只會印point，不會印child


print_all(root)
