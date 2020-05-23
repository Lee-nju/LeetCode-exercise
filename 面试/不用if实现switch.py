def get0():
    print(0)


def get1():
    print(1)


def get2():
    print(2)


def get3():
    print(3)


d = {0: get0, 1: get1, 2: get2, 3: get3}

for i in range(4):
    d[i]()
