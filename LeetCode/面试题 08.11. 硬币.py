mod = 1000000007


def waysToChange(n: int) -> int:
    """数学法"""
    if n <= 0:
        return 0
    if n < 5:
        return 1

    res = 0
    for i in range(n // 25 + 1):
        rest = n - 25 * i
        a0 = rest // 10
        b0 = (rest % 10) // 5
        res = res + (a0 + b0 + 1) * (a0 + 1) % mod
        res = res % mod

    return res


# 输入61 预期73
print(waysToChange(61))
