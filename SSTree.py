import math

# global variables
M = 4
m = 2
k = 2   # 維度


class SSNode:
    def __init__(self, leaf=False, radius=None, centroid=None):
        self.centroid = centroid        # turple
        self.radius = radius            # float
        self.children = []              # SSNode(對葉子節點來說，會是None)
        self.points = []                # (x, y) ((對內部節點來說，會是None))
        self.leaf = leaf                # boolean

    # For testing purposes
    def print_node_info(self):
        print("radius: ", self.radius, ", ", "leaf: ",
              self.leaf, ", ", "centroid: ", self.centroid)
        # print("leaf: ", self.leaf)
        # print("centroid: ", self.centroid)

    # 距離 (文章說是SS-Tree的結構參數(待確認))
    def distance(self, point1, point2):
        x = point1[0] - point2[0]
        y = point1[1] - point2[1]
        dis = math.sqrt(x*x + y*y)
        return dis

    # 是否跟目標點相交
    def intersectsPoint(self, point) -> bool:
        return self.distance(self.centroid, point) <= self.radius

    def mean(self, list):
        result = sum(list) / len(list)
        return result

    # 對node做update
    # 幹這邊有點難寫
    def updateBoundingEnvelope(self):
        # 取邊界中所有項目的中心點做平均
        # 葉節點取point平均
        if self.leaf:
            xsum = 0
            ysum = 0
            for i in self.points:
                xsum += i[0]
                ysum += i[1]
                self.centroid = (xsum/len(self.points), ysum/len(self.points))
        # 內節點取子節點平均
        else:
            xsum = 0
            ysum = 0
            for i in self.children:
                xsum += i[0]
                ysum += i[1]
                self.centroid = (xsum/len(self.points), ysum/len(self.points))

        # 半徑
        temp_radius = 0
        for i in self.children:
            dis = self.distance(self.centroid, i.centroid)
            if dis > temp_radius:
                temp_radius = dis
        self.radius = temp_radius

    # 回傳分支節點
    def findClosestChild(self, target):
        # 確保呼叫這個func的是node，而非leaf!
        # TODO: 呼叫前弄一個檢查機制

        # 適當更新最小距離和要回傳的點
        # 一個internal node至少有m個child，所以這些值至少會更新1次
        minDistance = float('inf')    # inf: 正無窮
        result = None
        # 循環瀏覽所有子節點
        for childNode in self.children:
            if self.distance(childNode.centroid, target) < minDistance:
                minDistance = self.distance(childNode.centroid, target)
                result = childNode
        # returns the closest one found
        return result

    # 分割(不確定，先假設所有點都已經對X軸做排序好了)
    def split(self):
        if self.leaf:
            n = 3
            newNode1 = SSNode(leaf=True, points=self.points[0:n-1])
            newNode2 = SSNode(leaf=True, points=self.points[n:])
        else:
            newNode1 = SSNode(leaf=False, points=self.children[0:n-1])
            newNode2 = SSNode(leaf=False, points=self.children[n:])
        return (newNode1, newNode2)

    # It returns the index of the direction along which the children of a node have maximum variance.
    # 沿著X軸做切割...
    # def directionOfMaxVariance(self):
    #     maxVariance = 0
    #     directionIndex = 0
    #     centroids = self.getEntriesCentroids()
    #     for i in k-1:
    #         if self.varianceAlongDirection(centroids, i) > maxVariance:
    #             maxVariance = self.varianceAlongDirection(centroids, i)
    #             directionIndex = i
    #     return directionIndex


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

    # Search the closest tree leaf to a target point
    def searchParentLeaf(self, node: SSNode, target):
        # 如果是leaf，則回傳
        if node.leaf:
            return node
        # 否則，我們就正在遍歷一個內部節點，並需找到下一步要去的分支
        else:
            child = node.findClosestChild(target)   # 決定要去的分支
            return self.searchParentLeaf(child, target)  # 遞迴遍歷我選擇的分支並返回結果

    # insert point
    def insert(self, node: SSNode, point):
        # Checks if node is a leaf:
        if node.leaf:
            if point in node.points:    # if it already contains the argument among its points
                return None
            node.points.append(point)   # Otherwise, adds the point to the leaf
            # recompute the centroid and radius for this leaf after adding the new point
            node.updateBoundingEnvelope()
            # After added a new point, we need to check whether this leaf now holds more than M points.
            if len(node.points) <= M:
                return None  # no more than M, we can return
        # Or if node isn't a leaf:
        else:
            # if it's a internal node, we need to call helper method find which branch to traverse
            closetChild = node.findClosestChild()
            # 遞迴遍歷樹並插入new point儲存操作結果，一旦分裂就是回傳那兩個node；否則，都是回傳null
            (newChild1, newChild2) = self.insert(closetChild, point)
            # 如果遞迴傳回null(意味closetChild沒有被分割)，則只需要更新現在的node的bounding envelope
            if newChild1 == None:
                node.updateBoundingEnvelope()
                return None
            # 意味closetChild已被分割成newChild1 & 2，需將他從子節點list中刪除
            else:
                node.children.remove(closetChild)
                node.children.append(newChild1)
                node.children.append(newChild2)
                node.children.sort()
                node.updateBoundingEnvelope()   # 對現在的node做update
                if len(node.children) <= M:  # 如果在數量範圍內，表示回溯工作完成
                    return None
        # If it gets here, it means that the node needs to be split: create two new nodes and return them.
        return node.split()

    # 當我們到了root需要對其進行分割時，我們需更新樹的根。
    # 必須在Tree class上執行，才能訪問樹的根

    # insert method for SSTree(split root)
    # takes a point and doesn’t return anything
    def insert2(self, point):
        (newChild1, newChild2) = self.insert(self.root, point)
        if newChild1 != None:
            self.root = SSNode(leaf=False, children=[
                               newChild1, newChild2])  # 這樣寫不確定餒!


def main():
    s1 = SSNode(True, 3, (8, 7))
    s1.print_node_info()

    ST = SSTree(2, 2, 4)
    print(ST.root.leaf)
    for i in range(10):
        ST.insert(ST.root, (i, i*2))
    # ST.insert(ST.root, (1, 2))


if __name__ == '__main__':
    main()
