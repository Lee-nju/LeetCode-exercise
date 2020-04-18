MAX_INT = 2147483647


def reverse(x: int) -> int:
    k = 1 if x < 0 else -1
    st = str(abs(x))[::-1]
    result = int(st)
    if result > MAX_INT:
        return 0
    else:
        return k * MAX_INT
