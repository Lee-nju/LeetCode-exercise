from LeetCode.TreeNode import TreeNode
from collections import deque


def deepSum(root):
    """
    问题：求最深一层节点的和

    Solution:
        利用层次遍历的方法，每次取出当前层所有节点，做值的累加和
        对于当前层的每个节点，如果存在子节点（左子或右子），将其加入队列
        当下一层节点为空时，表明当前是最后一层节点，将累加和输出即可

    :param root:
    :return:
    """
    if not root:
        return 0
    queue = deque()
    queue.append(root)
    while queue:
        # 上一层的节点数
        num = len(queue)
        sum = 0
        while num != 0:
            node = queue.popleft()
            sum = sum + node.val
            num = num - 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if len(queue) == 0:
            return sum

    return 0


print(deepSum(TreeNode(-1).list2Tree([1, 2, 3, 4, 5, 'null', 7])))
