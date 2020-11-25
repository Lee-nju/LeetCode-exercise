def genComb(n: int, k: int):
    comb = list(range(k))
    flag = True
    while flag:
        yield comb
        flag = False
        for i in range(1, k + 1):
            if comb[-i] < n - i:
                comb[-i] += 1
                for j in range(i - 1, 0, -1):
                    comb[-j] = comb[-i] + i - j
                flag = True
                break


for comb in genComb(5, 3):
    print(comb)
# g = genComb(5, 3)
# for i in range(10):
#     print(next(g))
