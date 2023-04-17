# import test2
import math
# print("hello test.")


# def pt():
#     print("you call me.")


# if __name__ == "__main__":
#     pt()
#     test2.outside.ano_pt()

# with open("C:/thesis/paper_code/test.txt") as f:
#     data = f.read()
#     print(data)


# data_list = [(2, 4), (8, 12), (9, 17), (15, 16), (23, 31), (26, 29), (35, 34), (40, 35), (42, 49), (51, 59),
#              (54, 46), (45, 55), (60, 75), (73, 76), (78, 63), (66, 77), (81, 85), (85, 91), (88, 96), (99, 94)]

data_list = [(2, 28), (10, 12), (12, 47), (19, 23), (23, 3), (26, 96), (35, 34), (41, 100), (42, 8), (51, 59),
             (54, 93), (61, 8), (68, 14), (73, 22), (73, 100), (80, 4), (81, 63), (81, 91), (82, 96), (83, 84)]
# data_list2 = []

# while (len(data_list) != 0):
#     temp = 878
#     result = None
#     for i in data_list:
#         # temp = 878
#         if i[0] + i[1] < temp:
#             temp = i[0] + i[1]
#             result = i
#         data_list2.append(i)
#         data_list.remove(i)

# print(data_list2)


# 資料分布前處理設計

centroid = (49.85, 49.25)


def distance(centroid, point):
    x = abs(centroid[0] - point[0])
    y = abs(centroid[1] - point[1])
    dis = math.sqrt(x*x + y*y)
    return dis


# def bubblesort(data):
#     # 定義資料長度
#     n = len(data)
#     for i in range(n-2):                   # 有 n 個資料長度，但只要執行 n-1 次
#         for j in range(n-i-1):             # 從第1個開始比較直到最後一個還沒到最終位置的數字
#             if data[j][0] + data[j][1] > data[j+1][0] + data[j+1][1]:        # 比大小然後互換
#                 data[j], data[j+1] = data[j+1], data[j]

def bubblesort(data):
    # 定義資料長度
    n = len(data)
    for i in range(n-2):                   # 有 n 個資料長度，但只要執行 n-1 次
        for j in range(n-i-1):             # 從第1個開始比較直到最後一個還沒到最終位置的數字
            if distance(data[j], centroid) > distance(data[j+1], centroid):        # 比大小然後互換
                data[j], data[j+1] = data[j+1], data[j]


bubblesort(data_list)
print(data_list)
