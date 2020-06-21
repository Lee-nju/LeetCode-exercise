from LeetCode.TreeNode import TreeNode


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        解题思路：递归
        1. 假设当前所在位置为node_i，那么"包含"node_i最大路径和可以这么计算:
            1.1 "左子树的最大路径和" 大于0，"包含"node_i最大路径 会将左子树的最大路径包含进来
            1.2 "右子树的最大路径和" 大于0，"包含"node_i最大路径 会将右子树的最大路径包含进来

        2. 假设当前所在位置为node_i，那么其父节点想要路过node_i，只能选择"包含"node_i 左子树 或者 右子树 或其 本身:
            2.1 "左子树的最大路径和" 和 "右子树的最大路径和" 都不大于0，"包含"node_i最大路径和为其本身的节点大小
            2.2 否则，"包含"node_i最大路径和为其本身再加左右子树较大者

        利用先序遍历的思想，先递归到子节点，不断根节点走，设置一个全局变量 MAX_PATH, 记录路过的所有节点的最大值

        :param root:
        :return:
        """
        # 这里利用了python的特性，虽然python没有引用，但列表作为一个可变对象，可以当作引用来使用
        MAX_PATH = [root.val]
        # 开始递归，最终的结果在 MAX_PATH 中
        self.maxNodePath(root, MAX_PATH)
        return MAX_PATH[0]

    def maxNodePath(self, root, MAX_PATH):
        """
        递归遍历：有两点任务
        1. 找到包含 root 的最大路径值
            如果 "左子树的最大路径和" 大于0，加上
            如果 "右子树的最大路径和" 大于0，加上
        2. 返回包含 root 的最大单边路径值
            当 "左子树的最大路径和" 和 "右子树的最大路径和" 都不大于0时，为 root 本身的值
            否则为，为 root 本身值再加左右子树较大者

        :param root:
        :param MAX_PATH:
        :return:
        """
        if root:
            # p_max 为包含root的最大路径和，ps_max 为包含root的最大"单边(single)"路径和
            p_max = ps_max = root.val
            # ls_max：包含左子节点的最大单边路径和 rs_max：包含右子节点的最大单边路径和
            ls_max = rs_max = 0

            # 左子树不为空，递归左子树，得到：包含左子节点的最大单边路径和
            if root.left:
                ls_max = self.maxNodePath(root.left, MAX_PATH)

            # 右子树不为空，递归右子树，得到：包含右子节点的最大单边路径和
            if root.right:
                rs_max = self.maxNodePath(root.right, MAX_PATH)

            # 大于0即加入双边路径
            if ls_max > 0:
                p_max = p_max + ls_max
            if rs_max > 0:
                p_max = p_max + rs_max

            # MAX_PATH[0] 更新为 MAX_PATH[0] 与 双边路径较大者
            MAX_PATH[0] = max(MAX_PATH[0], p_max)

            # 单边路径存在非负数 更新单边路径最大和
            if ls_max > 0 or rs_max > 0:
                ps_max = ps_max + max(ls_max, rs_max)

            return ps_max
        else:
            # 空节点的值0，MAX_PATH 也不更新
            return 0


t = TreeNode(-1).list2Tree([-10, 9, 20, 'null', 'null', 15, 7])
print(Solution().maxPathSum(t))

t = TreeNode(-1).list2Tree([-10, 18, 20, 'null', 'null', 15, 7])
print(Solution().maxPathSum(t))

t = TreeNode(-1).list2Tree([8, -10, 6, 6, 5, 3, -1])
print(Solution().maxPathSum(t))

t = TreeNode(-1).list2Tree([9, 6, -3, 'null', 'null', -6, 2, 'null', 'null', 2, 'null', -6, -6, -6])
print(Solution().maxPathSum(t))
