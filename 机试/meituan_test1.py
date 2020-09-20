while 1:
    s = input()
    if s != '':
        str = s.split()
        m, n = int(str[0]), int(str[1])
        result = 0
        for x in range(m, n + 1):
            k, tmp = x, set()
            while k > 0:
                tmp.add(k % 10)
                k = k // 10
            if len(tmp) < 6:
                continue
            ab, cd, ef = x // 10000, (x // 100) % 100, x % 100
            if ab + cd == ef:
                result += 1
        print(result)

    else:
        break
