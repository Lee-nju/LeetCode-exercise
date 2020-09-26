class Solution:
    def combine(self, n: int, k: int) -> [[int]]:
        comb = [i for i in range(1, k + 1)]
        result = [[x for x in comb]]
        i = k - 1
        while i >= 0:
            if comb[i] < n - (k - 1 - i):
                comb[i] += 1
                for j in range(i + 1, k):
                    comb[j] = comb[i] + j - i
                result.append([x for x in comb])
                i = k - 1
            else:
                i = i - 1
        return result


print(*Solution().combine(4, 2), sep='\n')
print(*Solution().combine(5, 3), sep='\n')
