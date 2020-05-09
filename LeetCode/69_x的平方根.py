def mySqrt(x: int) -> int:
    """
    暴力求解。
    可选的方法有：
    1. 利用其他函数逼近sqrt的求解
    2. 二分查找
    3. 牛顿迭代

    :param x:
    :return:
    """
    if x < 1:
        return 0
    if x == 1:
        return 1
    for i in range(1, x + 1):
        k = i * i
        if k == x:
            return i
        elif k > x:
            return i - 1


for i in range(10):
    print(mySqrt(i))
