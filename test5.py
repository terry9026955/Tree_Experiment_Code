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


p1 = Node((1, 2))
p2 = Node((3, 4))
p3 = Node((5, 6))

root = []
root.append(p1)
root.append(p2)
root.append(p3)

for i in root:
    print(i.centroid)
