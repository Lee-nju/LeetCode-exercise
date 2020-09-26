from LeetCode.TreeNode import TreeNode


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        mergeTree2(t1, t2)
        return t1


def mergeTree2(t1: TreeNode, t2: TreeNode):
    if not t1 and not t2:
        return
    if not t1:
        t1 = t2
        return
    if not t2:
        return
    t1.val += t2.val
    if t1.left and t2.left:
        mergeTree2(t1.left, t2.left)
    elif t2.left:
        t1.left = t2.left

    if t1.right and t2.right:
        mergeTree2(t1.right, t2.right)
    elif t2.right:
        t1.right = t2.right


# t1 = TreeNode(-1).list2Tree([1, 3, 2, 5])
# t2 = TreeNode(-1).list2Tree([2, 1, 3, 'null', 4, 'null', 7])
# t1 = TreeNode(-1).list2Tree([])
t2 = TreeNode(-1).list2Tree([1])
Solution().mergeTrees(None, t2).print_tree()
