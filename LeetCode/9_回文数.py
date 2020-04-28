def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    elif x < 10:
        return True
    y, m_int = 0, x
    while x != 0:
        y = y * 10 + x % 10
        x = x // 10

    return m_int == y


print(isPalindrome(1213443121))
