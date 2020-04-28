def singleNumbers(nums: [int]) -> [int]:
    d = dict()
    for x in nums:
        if x in d:
            d.pop(x)
        else:
            d[x] = 1

    return list(d.keys())


print(singleNumbers([4, 1, 4, 6]))
print(singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))
