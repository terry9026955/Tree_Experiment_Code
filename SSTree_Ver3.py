import math
import random

# random.randint(1,100)

data_list = []
for i in range(1000):
    data_list.append((random.randint(1, 100), random.randint(1, 100)))

data_list.sort()
# print(data_list)

threshold = 4


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


def distance(centroid, point):
    x = abs(centroid[0] - point[0])
    y = abs(centroid[1] - point[1])
    dis = math.sqrt(x*x + y*y)
    return dis


temp = []
leaf = []
centroid_list = []
radius_list = []


def region(df: list):
    df1 = []
    df2 = []
    # temp = []
    region_id = 0
    lenth = len(df)
    if lenth > threshold:
        df1 = df[0:int(lenth/2)]
        df2 = df[int(lenth/2):]
        temp.append(df1)
        temp.append(df2)
        region(df1)
        region(df2)

        # print(region1, region2)
        # temp[region_id] = df1
        # region_id += 1
        # temp[region_id] = df2
        # region_id += 1
    else:
        temp.remove(df)
        leaf.append(df)
        # region_id += 1
        return
    return region_id


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
        print("id: ", i, ", items: ", leaf[i], ", centroid: ",
              centroid_list[i], ", radius: ", radius_list[i])


def main():
    centroid = get_centroid(data_list)
    redius = get_radius(centroid)
    print("centroid: ", centroid, "radius: ", redius)

    id = region(data_list)
    # print("internal: ", temp)

    # for i in leaf:
    #     centroid_list.append(get_centroid(i))
    #     # print(get_centroid(i))
    # print(centroid_list)
    save_centroid(leaf)
    save_radius(leaf)

    print_all_leaf()


if __name__ == '__main__':
    main()


"""
if node.leaf:
    print(leaf.id, leaf.centroid, leaf.radius, leaf.items)
else:
    pass
"""
