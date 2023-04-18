# DFS遞迴方式分割地圖，每次分割會切成2個圓形的Maximum Bounding Envelope

import math
import random

# random.randint(1,100)

data_list = []
for i in range(20):
    data_list.append((random.randint(1, 100), random.randint(1, 100)))

# data_list = [(1, 4), (2, 4), (2, 7), (3, 15), (4, 4), (5, 2), (5, 8), (5, 18), (6, 5), (7, 11),
#              (7, 17), (9, 13), (11, 10), (12, 14), (14, 8), (15, 7), (18, 5), (18, 13), (20, 6), (20, 8)]
# 空間加大
# data_list = [(2, 28), (10, 12), (12, 47), (19, 23), (23, 3), (26, 96), (35, 34), (41, 100), (42, 8), (51, 59),    等等拿掉註解
#              (54, 93), (61, 8), (68, 14), (73, 22), (73, 100), (80, 4), (81, 63), (81, 91), (82, 96), (83, 84)]
# data_list2 = []

# for i in range(len(data_list)):
#     temp = 878
#     result = None
#     for i in data_list:
#         if i[0] + i[1] < temp:
#             result = i
#         data_list2.append(data_list[result])
#         data_list.remove(data_list[result])

# print(data_list2)

# 前處理設計(X+Y)
data_list = [(10, 12), (23, 3), (2, 28), (19, 23), (42, 8), (12, 47), (35, 34), (61, 8), (68, 14), (80, 4),
             (73, 22), (51, 59), (26, 96), (41, 100), (81, 63), (54, 93), (83, 84), (81, 91), (73, 100), (82, 96)]
# 前處理設計(距離)
# data_list = [(51, 59), (35, 34), (81, 63), (73, 22), (12, 47), (68, 14), (19, 23), (42, 8), (61, 8), (54, 93),
#              (83, 84), (41, 100), (81, 91), (2, 28), (26, 96), (23, 3), (80, 4), (10, 12), (73, 100), (82, 96)]

# 完美分布
# data_list = [(2, 4), (8, 12), (9, 17), (15, 16), (23, 31), (26, 29), (35, 34), (40, 35), (42, 49), (45, 55),
#              (51, 59), (54, 46), (60, 75), (66, 77), (73, 76), (78, 63), (81, 85), (85, 91), (88, 96), (99, 94)]

# data_list.sort()
print(data_list)

threshold = 5


def get_centroid(data_list):
    xsum = 0
    ysum = 0
    # max = data_list[len(data_list)-1]
    # min = data_list[0]
    for i in data_list:
        xsum += i[0]
        ysum += i[1]

    centroid = (xsum/len(data_list), ysum/len(data_list))
    return centroid


def get_radius(centroid):
    result = 0
    temp = None
    for i in data_list:
        temp = distance(centroid, i)
        if temp == None or temp > result:
            result = temp
    return result


def get_radius(centroid, df: list):
    result = 0
    temp = None
    for i in df:
        temp = distance(centroid, i)
        if temp == None or temp > result:
            result = temp
    return result


def distance(centroid, point):
    x = abs(centroid[0] - point[0])
    y = abs(centroid[1] - point[1])
    dis = math.sqrt(x*x + y*y)
    return dis


temp = []
leaf = []
centroid_list = []
radius_list = []


# 重覆面積公式
def intersected_area(p1, p2, r1, r2):
    d = math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]))
    if (d >= r1 + r2):
        return
    if (r1 > r2):
        tmp = r1
        r1 = r2
        r2 = tmp
    if (r2 - r1 >= d):
        return math.pi * r1 * r1

    ang1 = math.acos((r1 * r1 + d * d -
                     r2 * r2) / (2 * r1 * d))
    ang2 = math.acos((r2 * r2 + d * d -
                     r1 * r1) / (2 * r2 * d))
    return int((ang1 * r1 * r1) + (ang2 * r2 * r2) - (r1 * d * math.sin(ang1)))


# 分區策略: 選擇兩子圓重疊的最小範圍來劃分
# 1. 以最小重疊面積劃分 2. 以 兩圓半徑加總 - 兩圓中心直線距離之最小差來劃分

# 類KD-tree的分區策略


# def region(df: list):
#     df1 = []
#     df2 = []
#     # temp = []
#     region_id = 0
#     lenth = len(df)  # 準備對半切
#     if lenth > threshold:
#         df1 = df[0:int(lenth/2)]    #
#         df2 = df[int(lenth/2):]
#         temp.append(df1)
#         temp.append(df2)
#         region(df1)
#         region(df2)

#         print("df1: ", df1, "df2: ", df2)  # 註解掉
#         # temp[region_id] = df1   # 註解掉
#         # region_id += 1
#         # temp[region_id] = df2   # 註解掉
#         # region_id += 1
#     else:
#         # temp.remove(df)   # 註執行
#         leaf.append(df)   # 註執行
#         # region_id += 1
#         return

# 使用分區策略的分割


def region2(df: list):
    df1 = []
    df2 = []
    # temp = []
    split_index = findSplit(df)
    if len(df) > threshold:
        df1 = df[0:int(split_index)]    #
        df2 = df[int(split_index):]
        temp.append(df1)
        temp.append(df2)
        region2(df1)
        region2(df2)

        print("df1: ", df1, "df2: ", df2)  # 紀錄分區

        # temp[region_id] = df1   # 註解掉
        # region_id += 1
        # temp[region_id] = df2   # 註解掉
        # region_id += 1
    else:
        temp.remove(df)   # 註執行
        leaf.append(df)   # 註執行
        # region_id += 1
        return


def findSplit(df: list):
    df1 = []
    df2 = []
    split_index = 2  # 預設小m
    tempArea = 8787  # 紀錄最小面積
    splitArea = 8787    # 回傳最小面積
    former = int(len(df) * 0.4)
    lenth = int(len(df)) - 2
    for i in range(former, lenth):
        df1 = df[0:int(i)]    #
        df2 = df[int(i):]
        circle1_cen = get_centroid(df1)
        circle2_cen = get_centroid(df2)
        circle1_rad = get_radius(circle1_cen, df1)
        circle2_rad = get_radius(circle2_cen, df2)

        # 分區策略1:
        tempArea = intersected_area(
            circle1_cen, circle2_cen, circle1_rad, circle2_rad)
        if (tempArea == None):
            return i

        # 分區策略2:
        # tempArea = abs((circle1_rad + circle2_rad) -
        #                distance(circle1_cen, circle2_cen))

        # 紀錄重疊最小的時候
        if tempArea < splitArea:
            splitArea = tempArea
            split_index = i

    return split_index


def save_centroid(leaf):
    for i in leaf:
        centroid_list.append(get_centroid(i))
        # print(get_centroid(i))
    # print("centroid list: ", centroid_list)


def save_radius(leaf):
    for i in leaf:
        cen = get_centroid(i)
        result = 0
        temp = None
        for j in i:
            temp = distance(cen, j)
            if temp == None or temp > result:
                result = temp
        result
        radius_list.append(result)
    # print("radius_list: ", radius_list)


def print_all_leaf():
    idx = len(leaf)
    print("leaf_numbers: ", len(leaf))
    for i in range(idx):
        print("Leaf id: ", i, ", items: ", leaf[i], ", centroid: ",
              centroid_list[i], ", radius: ", radius_list[i])


def main():

    centroid = get_centroid(data_list)
    redius = get_radius(centroid, data_list)
    print("centroid: ", centroid, "radius: ", redius)

    # print("not using split method")

    # region(data_list)

    # print(findSplit(data_list))   # 測試split的index
    # print("using split method")
    region2(data_list)
    # print("internal: ", temp)

    # for i in leaf:
    #     centroid_list.append(get_centroid(i))
    #     # print(get_centroid(i))
    # print(centroid_list)
    save_centroid(leaf)
    save_radius(leaf)

    print_all_leaf()

    # print(intersected_area((0, 0), (0, 5), 3, 3))


if __name__ == '__main__':
    main()


"""
if node.leaf:
    print(leaf.id, leaf.centroid, leaf.radius, leaf.items)
else:
    pass
"""
