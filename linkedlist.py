class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def print_data(self):
        print("data: ", self.data)
        # print("next: ", self.next)


# 從root開始traversal
def print_all_node(root):
    i = root
    while True:
        if i.next != None:  # 遍歷節點
            i.print_data()
            i = i.next
        else:               # 遇到最後一個node時要跳出
            i.print_data()
            break


def main():
    # 建立節點
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    # 把節點串起來
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # 從root開始traversal
    print("start from node1")
    print_all_node(node1)
    # 其他點開始
    print("start from node3")
    print_all_node(node3)

    # # list練習
    # print("list[:] test...")
    # test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # t = 5
    # x = test_list[0: t]                 # [1, 2, 3, 4, 5]
    # y = test_list[t: len(test_list)]    # [6, 7, 8, 9]
    # print(x)
    # print(y)


if __name__ == '__main__':
    main()
