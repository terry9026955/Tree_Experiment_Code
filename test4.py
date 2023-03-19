gg = []
gg.append(87)
gg.append(78)

print(gg)

gg.sort()
print(gg)

gg.append(66)
print(gg)


x = []
y = []
if (len(gg) == 3):
    gg.sort()
    x = gg[0:2]
    y = gg[2:3]

print("after split...")
print(x, y)
