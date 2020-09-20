def subsets(nums: [int]) -> [[int]]:
    res = [[]]
    for i in range(1, len(nums) + 1):
        index_comb = [j for j in range(i)]
        res.append([nums[j] for j in index_comb])
        while next_comb(index_comb, len(nums)):
            tmpSet = [nums[j] for j in index_comb]
            if tmpSet not in res:
                res.append(tmpSet)

    return res


def next_comb(comb, n):
    hasNextComb = False
    for i in range(len(comb) - 1, -1, -1):
        if comb[i] < n - (len(comb) - i):
            comb[i] += 1
            for j in range(i + 1, len(comb)):
                comb[j] = comb[i] + j - i

            hasNextComb = True
            break

    return hasNextComb


print(*subsets([1, 2, 3]), sep='\n')
