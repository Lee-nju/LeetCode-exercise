def intToRoman(num: int) -> str:
    res = []
    toRoman(num, res)
    s = ''.join(res)
    return s


def toRoman(num: int, res: [str]):
    if num == 0:
        return
    if num == 4:
        res.append('IV')
    elif num == 9:
        res.append('IX')
    elif 40 <= num < 50:
        res.append('XL')
        toRoman(num - 40, res)
    elif 90 <= num < 100:
        res.append('XC')
        toRoman(num - 90, res)
    elif 400 <= num < 500:
        res.append('CD')
        toRoman(num - 400, res)
    elif 900 <= num < 1000:
        res.append('CM')
        toRoman(num - 900, res)
    elif num < 5:
        res.extend(['I'] * num)
    elif num < 10:
        res.append('V')
        res.extend(['I'] * (num - 5))
    elif num < 50:
        res.extend(['X'] * (num // 10))
        toRoman(num % 10, res)
    elif num < 100:
        res.append('L')
        toRoman(num - 50, res)
    elif num < 500:
        res.extend(['C'] * (num // 100))
        toRoman(num % 100, res)
    elif num < 1000:
        res.append('D')
        toRoman(num - 500, res)
    else:
        res.extend(['M'] * (num // 1000))
        toRoman(num % 1000, res)


print(intToRoman(3))
print(intToRoman(4))
print(intToRoman(9))
print(intToRoman(58))
print(intToRoman(1994))
