from LeetCode.TreeNode import TreeNode
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            # 上一层的节点数
            num_of_node = len(queue)
            cur = []
            while num_of_node > 0:
                node = queue.popleft()
                cur.append(node.val)
                # 每次取出时，将子节点加入队列
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                num_of_node = num_of_node - 1

            res.append(cur)

        return res


tree = TreeNode(-1).list2Tree([3, 9, 20, 'null', 'null', 15, 7])
print(Solution().levelOrder(tree))
