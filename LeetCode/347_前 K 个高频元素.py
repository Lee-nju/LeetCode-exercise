def topKFrequent(nums: [int], k: int) -> [int]:
    if not nums:
        return []

    tmp, res, fre = [], [], {}
    for x in nums:
        if x in fre:
            fre[x] = fre[x] + 1
        else:
            fre[x] = 1

    tmp = sorted(fre.items(), key=lambda x: x[1], reverse=True)
    print(tmp)
    for i in range(k):
        res.append(tmp[i][0])
    return res


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([3, 0, 1, 0], 1))
