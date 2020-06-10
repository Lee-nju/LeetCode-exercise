def merge_sort(num: [int]):
    # 当数组
    if not num or len(num) < 2:
        return
    else:
        merge_process(num, 0, len(num) - 1)


def merge_process(num: [int], l: int, r: int):
    """
    递归函数，将待排序数组不断切割成更小的数组

    :param num:
    :param l:
    :param r:
    :return:
    """
    if l == r:
        return
    else:
        # 算中间位置
        mid = l + ((r - l) >> 1)
        # 排左边部分 num[l..mid]
        merge_process(num, l, mid)
        # 排右边部分 num[mid+1..r]
        merge_process(num, mid + 1, r)
        # 合并左边和右边部分
        merge(num, l, mid, r)


def merge(num: [int], l: int, mid: int, r: int):
    """
    将 l..mid 和 mid+1..r 位置的内容合并至 num[l..r]

    :param num:
    :param l:
    :param mid:
    :param r:
    :return:
    """
    # 额外空间数组，放置合并后的数组 num[l..r]
    tmp = [0] * (r - l + 1)
    i = 0
    p1 = l
    p2 = mid + 1
    while p1 <= mid and p2 <= r:
        # 保证归并是稳定的排序
        if num[p1] <= num[p2]:
            tmp[i] = num[p1]
            p1 = p1 + 1
        else:
            tmp[i] = num[p2]
            p2 = p2 + 1
        i = i + 1

    # 将剩余的部分直接加到辅助空间数组上
    while p1 <= mid:
        tmp[i] = num[p1]
        i = i + 1
        p1 = p1 + 1

    while p2 <= r:
        tmp[i] = num[p2]
        i = i + 1
        p2 = p2 + 1

    # 复制回原数组 num[l..r]
    for i in range(l, r + 1):
        num[i] = tmp[i - l]


num = [7, 3, 12, 2, 4, 1, 5, 9, 7]
merge_sort(num)
print(num)
