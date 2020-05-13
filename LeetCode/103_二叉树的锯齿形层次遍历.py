from LeetCode.TreeNode import TreeNode
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        # 存放结果
        res = []
        # 从左往右遍历时flag为true，从右往左时为false
        flag = True
        while queue:
            num_of_node = len(queue)
            cur = []
            while num_of_node > 0:
                node = queue.popleft()
                cur.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                num_of_node = num_of_node - 1

            if flag:
                res.append(cur)
                flag = False
            else:
                res.append(cur[::-1])
                flag = True

        return res


tree = TreeNode(-1).list2Tree([3, 9, 20, 'null', 'null', 15, 7])
print(Solution().zigzagLevelOrder(tree))
