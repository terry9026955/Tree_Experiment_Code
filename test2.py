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
