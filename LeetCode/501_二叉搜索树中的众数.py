from LeetCode.TreeNode import TreeNode


class Solution:
    def findMode(self, root: TreeNode) -> [int]:
        res = []
        common_times = -1
        tmp_times = tmp_value = -2
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop(-1)
                if node.val != tmp_value:
                    if tmp_times > common_times:
                        res = [tmp_value]
                        common_times = tmp_times
                    elif tmp_times == common_times:
                        res.append(tmp_value)
                    tmp_value = node.val
                    tmp_times = 1
                else:
                    tmp_times += 1
                node = node.right

        if tmp_times > common_times:
            res = [tmp_value]
        elif tmp_times == common_times:
            res.append(tmp_value)

        return res


print(Solution().findMode(TreeNode(-1).list2Tree([1, 'null', 2, 2])))
