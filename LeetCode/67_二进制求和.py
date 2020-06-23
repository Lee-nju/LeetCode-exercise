def addBinary(a: str, b: str) -> str:
    """
    解题思路：
    1. 系统的二进制加法
        1.1 int(str, 2): 将str按2进制看待，转换成10进制整数
        1.2 bin(integer): 将10进制整数转成2进制字符串
        1.3 去掉二进制字符串前置字符 '0b'

    2. 指针法: 注意多一个进位即可

    :param a:
    :param b:
    :return:
    """
    return bin(int(a, 2) + int(b, 2))[2:]


# print(addBinary(a="1010", b="1011"))
print(int("1010", 2))
# print(bin(int("1010", 2) + int('1011', 2)))
