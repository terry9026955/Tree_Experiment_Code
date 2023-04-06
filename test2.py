class outside:
    def ano_pt():
        print("from another file.")


# in test
a = [1, 2, 3]
if 1 in a:
    print("yes!")
else:
    print("no!")

b = [(1, 2), (3, 4)]
print((1, 2) in b)  # True
print(len(b))

# delete test
c = [3, 6, 9]
print("before: ", c)
c.remove(3)
print("after: ", c)
c.append(2)
c.sort()
print("sorted: ", c)

# remove variable test
d = [1, 2, 3]
tt = 1
d.remove(tt)
print("after remove variable: ", d)
