import rNode as rnode


class RTree:
    def __init__(self, m=2, M=4) -> None:
        # 用(m=2, M=4)預設值建立空的R-Tree
        self.root = None
        self.m = m
        self.M = M

    def add(self, rectangle, ident=None):
        # 將矩形插入具有(隨意的)識別碼的適當位置
        if self.root is None:
            self.root = rnode.RNode(self.M, rectangle, None)
            self.root.addEntry(self.M, rectangle, ident)
        else:
            # I1[針對新紀錄找尋位置]喚起chooseLeaf
            # 以在其中選擇樹葉節點L並放置E。傳回樹葉的路徑。
            path = self.root.chooseLeaf(rectangle, [self.root])
            n = path[-1]
            del path[-1]

            # I2[將記錄加入樹葉節點]如果L有空機容納另外的項目，則安裝E。
            # 否則喚起SplitNode取得含有E的L與LL以及L的舊項目。
            newLeaf = None
            if n.count < self.M:
                n.addEntry(self.M, rectangle, ident)
            else:
                newLeaf = n.split(rnode.RNode(
                    self.M, rectangle, ident, 0), self.m, self.M)

            # I3[向上傳送變更]喚起L的AdjustTree，另外如果執行分開動作則傳遞LL。
            newNode = self.adjustTree(n, newLeaf, path)

            # I4[增加樹的高度]如果節點的分散波及導致根要分開，
            # 則建立其子節點是兩個結果節點的新根。
            if newNode:
                newRoot = rnode.RNode(self.M, level=newNode.level + 1)
                newRoot.addRNode(newNode)
                newRoot.addRNode(self.root)
                self.root = newRoot

    def range(self, target):
        # 傳回與目標重疊的所有合格(node,0,True) 或 (rect,id,False)的產生器
        if self.root:
            return self.root.range(target)
        else:
            return None


# 實驗
def main():
    # 建立degree是3的BTree
    R = RTree()
    R.add()


if __name__ == '__main__':
    main()
