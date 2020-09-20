def permuteUnique(nums: [int]) -> [[int]]:
    res = []
    recursivePermute(res, [], nums)
    return res


def recursivePermute(res: [[int]], pre_num: [int], remain_num: [int]):
    if len(remain_num) == 1:
        tmp = [*pre_num, remain_num[0]]
        if tmp not in res:
            res.append(tmp)
    else:
        for i in range(len(remain_num)):
            tmp = [*remain_num[:i], *remain_num[i + 1:]]
            recursivePermute(res, [*pre_num, remain_num[i]], tmp)


a = [1, 2, 3]
print(*permuteUnique(a), sep='\n')
