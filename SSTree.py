import math


class SSNode:
    def __init__(self, radius, leaf=False, centroid=None):
        self.centroid = centroid      # turple
        self.radius = radius    # float
        self.children = []         # SSNode(對葉子節點來說，會是None)
        self.points = []        # (x, y) ((對內部節點來說，會是None))
        self.leaf = leaf        # boolean

    def print_node_info(self):
        pass
        print("radius: ", self.radius, ", ", "leaf: ",
              self.leaf, ", ", "centroid: ", self.centroid)
        # print("leaf: ", self.leaf)
        # print("centroid: ", self.centroid)

    # 距離
    def distance(self, point1, point2):
        x = point1[0] - point2[0]
        y = point1[1] - point2[1]
        dis = math.sqrt(x*x + y*y)
        return dis

    # 是否跟目標點相交
    def intersectsPoint(self, point) -> bool:
        return self.distance(self.centroid, point) <= self.radius


class SSTree:
    def __init__(self, k, m, M):
        self.root = SSNode(True)
        self.m = m  # min
        self.M = M  # max
        self.k = k  # each data entry's dimension

    # Search points: node是節點(球體)，target是XY座標
    def search(self, node: SSNode, target):
        if node.leaf:   # 如果是葉節點
            for point in node.points:
                if point == target:
                    print("Found point")
                    return node
        else:
            # 對每個子節點childNode，檢查其中心點與目標點之間的距離
            # 如果這個距離小於childNode的邊界包圍半徑(bounding envelope’s radius)，則我們就遞迴遍歷childNode
            for childNode in node.children:
                # 檢查childNode是否可以包含目標，是的話就在childNode的branch上進行遞迴搜尋
                if childNode.intersectsPoint(target):
                    result = self.search(childNode, target)
                    if result != None:
                        print("Found point")
                        return result
        # 如果當前節點沒有子節點可以包含目標，或葉子節點上沒有與目標匹配的點
        return None


def main():
    s1 = SSNode(3, True, (8, 7))
    s1.print_node_info()


if __name__ == '__main__':
    main()
