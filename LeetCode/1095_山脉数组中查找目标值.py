class MountainArray:
    def __init__(self, l):
        self.__ll = l

    def get(self, index: int) -> int:
        return self.__ll[index]

    def length(self) -> int:
        return len(self.__ll)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        """
        1. 先找峰顶，
        2. 在峰顶左边区间找（递增），找到返回，没找到进入3
        3. 在峰顶右边区间找（递减），找到返回下标，否则返回-1
        :param target:
        :param mountain_arr:
        :return:
        """
        n = mountain_arr.length()
        peak = self.search_peak(0, n - 1, mountain_arr)
        if mountain_arr.get(peak) == target:
            return peak
        res = self.find_sorted_arr(mountain_arr, 0, peak - 1, target)
        if res != -1:
            return res

        return self.find_reversed_arr(mountain_arr, peak + 1, n - 1, target)

    def search_peak(self, left, right, arr) -> int:
        """
        1. 返回[left,right]的峰顶位置
        :param left:
        :param right:
        :param arr:
        :return:
        """
        # 循环结束时，一定有：left==right
        while left < right:
            # mid 取下界
            mid = left + (right - left) // 2
            if arr.get(mid) < arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        return left

    def find_sorted_arr(self, arr, left, right, target) -> int:
        """
        2. 在峰顶左区间找
        :param arr:
        :param left:
        :param right:
        :param target:
        :return:
        """
        # 循环结束时：left==right
        while left < right:
            mid = left + (right - left) // 2
            if arr.get(mid) < target:
                left = mid + 1
            else:
                right = mid

        if arr.get(left) == target:
            return left
        else:
            return -1

    def find_reversed_arr(self, arr, left, right, target) -> int:
        """
        3. 在峰顶右区间找
        :param arr:
        :param left:
        :param right:
        :param target:
        :return:
        """
        # 循环结束时：left==right
        while left < right:
            # 取上界[left,right(mid)]
            mid = left + (right - left + 1) // 2
            if arr.get(mid) < target:
                right = mid - 1
            else:
                left = mid

        if arr.get(left) == target:
            return left
        else:
            return -1


arr = MountainArray([1, 3, 5, 4, 3, 2, 1])
print(Solution().findInMountainArray(2, arr))
