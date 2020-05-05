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
