# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        关键的是列表的表示与操作
        难点在于将num表示成ListNode对象，这点可通过debug发现

        pass
        """
        num1 = num2 = 0
        k = 0
        while l1:
            # print(l1.val)
            num1 = num1 + l1.val * (10 ** k)
            l1 = l1.next
            k = k + 1

        k = 0
        while l2:
            num2 = num2 + l2.val * (10 ** k)
            l2 = l2.next
            k = k + 1

        num = str(num1 + num2)
        num = [int(num[i]) for i in range(len(num) - 1, -1, -1)]

        dummyRoot = ListNode(0)
        ptr = dummyRoot
        for number in num:
            ptr.next = ListNode(number)
            ptr = ptr.next

        ptr = dummyRoot.next
        # print(result)
        return ptr


# x = ListNode([2, 4, 3])
# while x.next != None:
#     print(x.val)
#     x = x.next

v = '678'
num = [int(v[i]) for i in range(len(v) - 1, -1, -1)]
dummyRoot = ListNode(0)
ptr = dummyRoot
for number in num:
    ptr.next = ListNode(number)
    ptr = ptr.next

ptr = dummyRoot.next
print(ptr)
