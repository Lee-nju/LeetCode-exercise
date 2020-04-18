INT_MAX = 2147483647
INT_MIN = -2147483648


def myAtoi(str: str) -> int:
    str = str.strip()
    if not str:
        return 0

    k = -1 if str[0] == '-' else 1
    try:
        if str[0] != '+' and str[0] != '-' and not str[0].isdigit():
            return 0
    except:
        return 0

    # i是第一个不是数字的字符的下标，j是第一个是数字的字符的下标；'-+-8'：j=3,i=4
    i, j, n = 0, 0, len(str)
    if str[0] == '+' or str[0] == '-':
        i = 1
        j = 1

    while i < n:
        if not str[i].isdigit():
            break
        i = i + 1

    s = str[j: i]
    try:
        result = int(s) * k
    except:
        return 0

    if result > INT_MAX:
        return INT_MAX
    elif result < INT_MIN:
        return INT_MIN
    else:
        return result


print(myAtoi("+902"))
