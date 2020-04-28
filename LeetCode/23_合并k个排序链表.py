class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists: [ListNode]) -> ListNode:
    """
    暴力求解法：遍历所有链表，将每个遍历到的值放入数组，利用快速排序给数组排序，再利用数组的元素生成一个有序链表
    时间复杂度：O(N logN) 空间复杂度：O(N)

    pass
    """
    if not lists:
        return None

    k = len(lists)
    res = []
    for i in range(k):
        node = lists[i]
        while node:
            res.append(node.val)
            node = node.next

    if not res:
        return None

    res.sort()
    merge = ListNode(res[0])
    node = merge
    for x in res[1:]:
        node.next = ListNode(x)
        node = node.next

    return merge
