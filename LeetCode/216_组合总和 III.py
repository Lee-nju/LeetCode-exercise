def combinationSum3(k: int, n: int) -> [[int]]:
    res, tmp = [], [i for i in range(1, k)]
    i = 1

    return res


def next_arr(res, tmp, k, i, n):
    if i < k and tmp[-i] < 10 - i:
        j = 1
        while j <= i:
            s = sum(tmp)
            if tmp[-1] < n - s <= 9:
                res.append([*tmp, n - s])
            elif tmp[-1] >= n - s:
                j = j + 1
            if j < k:
                tmp[-j] = tmp[-j] + 1
                for m in range(j - 1, 0, -1):
                    tmp[-m] = tmp[-(m + 1)] + 1


# print(combinationSum3(3, 7))
# print(combinationSum3(3, 9))
print(combinationSum3(3, 15))
# print(combinationSum3(5, 20))
