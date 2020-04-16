def merge(intervals: [[int]]) -> [[int]]:
    """
    one sumbit pass

    """
    if not intervals:
        return []

    i, j, n = 0, 1, len(intervals)
    # 按列表的第一个元素给列表排序
    intervals.sort()
    result = []
    while i < n:
        # 如果j超出下标，说明i是最后一个元素
        if j > n - 1:
            result.append(intervals[i])
            break
        # interval[i] 为当前的区间，往后拓展试试
        cInterval = intervals[i]
        # 如果前一区间右边界大于等于后一区间右边界，说明是包含关系
        if cInterval[1] >= intervals[j][1]:
            j = j + 1
        # 如果前一区间右边界大于等于后一区间左边界，说明是相交的关系，更新当前的区间的右边界
        elif cInterval[1] >= intervals[j][0]:
            cInterval[1] = intervals[j][1]
        else:
            # 如果前一区间右边界小于后一区间左边界，说明无重叠部分，将当前区间加入最终结果，并更新下标
            result.append(cInterval)
            i, j = j, j + 1

    return result


value = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(value))
