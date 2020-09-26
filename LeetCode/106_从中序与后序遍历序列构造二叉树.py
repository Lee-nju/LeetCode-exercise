from LeetCode.TreeNode import TreeNode


class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        """
        Solution:
        1. 如果 inorder 列表为空，返回 None
        2. 如果 inorder 长度为 1，直接返回
        3. 由 postorder[-1] 拿到根节点
        4. 找到根节点在 inorder[] 中的位置
        5. 根据 inorder 和 postorder 列表等长的特性
            1. 递归左子树
            2. 赌鬼右子树

        :param inorder:
        :param postorder:
        :return:
        """

        if not inorder:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(postorder[-1])
        sep = inorder.index(postorder[-1])
        if sep == 0:
            root.right = self.buildTree(inorder[1:], postorder[:-1])
        elif sep == len(inorder) - 1:
            root.left = self.buildTree(inorder[:-1], postorder[:-1])
        else:
            root.left = self.buildTree(inorder[:sep], postorder[:sep])
            root.right = self.buildTree(inorder[(sep + 1):], postorder[sep: -1])
        return root


Solution().buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]).print_tree()
Solution().buildTree([2, 3, 1], [3, 2, 1]).print_tree()
Solution().buildTree([1, 2, 3, 4], [2, 1, 4, 3]).print_tree()
