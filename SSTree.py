class SSNode:
    def __init__(self, radius, leaf=False, centroid=None):
        self.centroid = centroid      # turple
        self.radius = radius    # float
        self.child = []         # SSNode
        self.points = []        # (x, y)
        self.leaf = leaf        # boolean

    def print_node_info(self):
        pass
        print("radius: ", self.radius, ", ", "leaf: ",
              self.leaf, ", ", "centroid: ", self.centroid)
        # print("leaf: ", self.leaf)
        # print("centroid: ", self.centroid)


class SSTree:
    def __init__(self, k, m, M):
        self.root = SSNode(True)
        self.m = m
        self.M = M
        self.k = k

    # def insert(self, node):
    #     root = self.root


def main():
    s1 = SSNode(3, True, (8, 7))
    s1.print_node_info()


if __name__ == '__main__':
    main()
