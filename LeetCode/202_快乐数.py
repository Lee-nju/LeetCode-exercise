def isHappy(n: int) -> bool:
    x = n
    mid_value = []
    j = 0
    while x != 1:
        j = j + 1
        if x in mid_value:
            return False
        mid_value.append(x)
        a, x = x, 0
        while a != 0:
            x = x + (a % 10) ** 2
            a = a // 10

    return True


# print(isHappy(1))
print(isHappy(19))
print(isHappy(2))
