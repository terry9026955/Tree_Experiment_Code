import math


def distance(centroid, point):
    x = abs(centroid[0] - point[0])
    y = abs(centroid[1] - point[1])
    dis = math.sqrt(x*x + y*y)
    return dis


def get_radius(centroid, df: list):
    result = 0
    temp = None
    for i in df:
        temp = distance(centroid, i)
        if temp == None or temp > result:
            result = temp
    return result


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


datalist = [(10, 12), (23, 3), (2, 28), (19, 23), (42, 8),
            (12, 47), (35, 34), (61, 8), (68, 14), (80, 4), (73, 22)]

cen = get_centroid(datalist)
rad = get_radius(cen, datalist)
print("cen: ", cen, " \nrad: ", rad)
