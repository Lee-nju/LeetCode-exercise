from LeetCode.TreeNode import TreeNode


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> [[int]]:
        """
        Solution:
            深度优先遍历。
            记录路径和，如果 sum == root.val 且当前 root 为叶子节点，将路径添加至总集合

        :param root:
        :param sum:
        :return:
        """
        if not root:
            return []
        res = []

        def pathSum2(root, sum, path):
            tmp = [*path, root.val]
            if sum == root.val and not root.left and not root.right:
                res.append(tmp)
            if root.left:
                pathSum2(root.left, sum - root.val, tmp)
            if root.right:
                pathSum2(root.right, sum - root.val, tmp)

        pathSum2(root, sum, [])
        return res


tree = TreeNode(-1).list2Tree([5, 4, 8, 11, 13, 4, 'null', 7, 2, 'null', 'null', 5, 1])
print(*Solution().pathSum(tree, 22), sep='\n')
