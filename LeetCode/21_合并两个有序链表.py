# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def init_list(l: list) -> ListNode:
    res = node = ListNode(l[0])
    for x in l[1:]:
        node.next = ListNode(x)
        node = node.next
    return res


def m_print(node: ListNode):
    l = []
    while node:
        l.append(node.val)
        node = node.next

    print(l)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        res = node = None
        while l1 and l2:
            if l1.val <= l2.val:
                if node:
                    node.next = l1
                    node = node.next
                else:
                    node = l1
                    res = node
                l1 = l1.next

            else:
                if node:
                    node.next = l2
                    node = node.next
                else:
                    node = l2
                    res = node
                l2 = l2.next

        if l1:
            node.next = l1
        else:
            node.next = l2

        return res


l1 = init_list([1, 2, 4])
l2 = init_list([1, 3, 4])
m_print(Solution().mergeTwoLists(l1, l2))
