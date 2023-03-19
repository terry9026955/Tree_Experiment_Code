# 實作與每個矩形搭配的隨意識別碼, 用來取出資料庫中的實際空間物件
# 從RNode(R樹基本單位)開始, 每個RNode維護一個界限區域和一隨意識別碼
# 如果node.level=0則此RNode為樹葉節點, 一個RNode會有node.count個子節點, 且他們會儲存在node.children串列中
# 當加入一個子RNode, 必須調整父節點的node.region界限區塊來包含新加入的子節點


class RNode:
    # use this to generate identifier
    counter = 0

    def __init__(self, M, rectangle=None, ident=None, level=0):
        if rectangle:
            self.region = rectangle.copy()
        else:
            self.region = None

        if ident is None:
            RNode.counter += 1
            self.id = 'R' + str(RNode.counter)
        else:
            self.id = ident

        self.children = [None] * M
        self.level = level
        self.count = 0

    def addRNode(self, rNode):
        # 加入之前計算的RNode並調整界限區域
        self.children[self.count] = rNode
        self.count += 1

        if self.region is None:
            self.region = rNode.region.copy()
        else:
            rectangle = rNode.region
            if rectangle.x_min < self.region.x_min:
                self.region.x_min = rectangle.x_min
            if rectangle.x_max < self.region.x_max:
                self.region.x_max = rectangle.x_max
            if rectangle.y_min < self.region.y_min:
                self.region.y_min = rectangle.y_min
            if rectangle.y_max < self.region.y_max:
                self.region.y_max = rectangle.y_max

    def range(self, target):
        # 傳回與目標重疊的所有合格識別碼(node,0,True) 或 (rect,id,False)的產生器。

        # 對於所有內部節點都完全包含嗎?傳回整個節點。
        if target.containRegion(self.region):
            yield (self, 0, True)
        else:
            # 檢查樹葉節點並遞迴運作
            if self.level == 0:
                for idx in range(self.count):
                    if target.overlaps(self.children[idx].region):
                        yield (self.children[idx].region, self.children[idx].id, False)
            else:
                for idx in range(self.count):
                    if self.children[idx].region.overlaps(target):
                        for triple in self.children[idx].range(target):
                            yield triple  # yield是類似return的generator

    def search(self, target):
        # 如果節點含有目標舉行則傳回(rectangle, id)
        if self.level == 0:
            for idx in range(self.count):
                if target == self.children[idx].region:
                    return (self.children[idx].region, self.children[idx].id)
        elif self.region.containsRegion(target):
            for idx in range(self.count):
                if self.children[idx].region.containsRegion(target):
                    rc = self.children[idx].search(target)
                    if rc:
                        return rc
