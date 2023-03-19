# Create a node
class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []


# Tree
class BTree:
    # t表示minimum degree, 除root之外的node都至少要有t-1個keys, root通常含1個key.
    # 所有nodes(含root)通常包含至多(2t-1)個keys
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    # Insert node (吃一個tuple(兩個keys))
    def insert(self, k):
        root = self.root
        # 插入時，如果node的空間滿了，要做分割:
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    # Insert nonfull(如果插入時空間沒滿，吃root還有tuple)
    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    # Split the child
    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

# Print the tree(吃BTreeNode)
    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:   # child指向一個BTreeNode
                self.print_tree(i, l)

# Search key in the tree
    def search_key(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i][0]:
                i += 1
            if i < len(x.keys) and k == x.keys[i][0]:
                return (x, i)
            elif x.leaf:
                return None
            else:
                return self.search_key(k, x.child[i])

        else:
            return self.search_key(k, self.root)


def main():
    # 建立degree是3的BTree
    B = BTree(3)

    for i in range(10):
        B.insert((i, 2 * i))

    # 手動插入
    # B.insert((100, 100))
    # B.insert((35, 65))
    # B.insert((130, 180))
    # B.insert((10, 20))
    # B.insert((40, 50))
    # B.insert((70, 80, 90))
    # B.insert((110, 120))
    # B.insert((140, 160))
    # B.insert((190, 240, 260))
    # B.insert((87, 88))

    B.print_tree(B.root)

    if B.search_key(40) is not None:
        print("\nFound")
    else:
        print("\nNot Found")

    print("print root's keys:")
    print(B.root.keys)


if __name__ == '__main__':
    main()
