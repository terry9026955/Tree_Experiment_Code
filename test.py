import test2

print("hello test.")


def pt():
    print("you call me.")


if __name__ == "__main__":
    pt()
    test2.outside.ano_pt()

with open("C:/thesis/paper_code/test.txt") as f:
    data = f.read()
    print(data)
