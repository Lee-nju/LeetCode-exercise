import json
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rightSideView(root: TreeNode) -> [int]:
    """
    利用广度优先遍历，右视图看到的一定是每一层的最右节点
    1. k1表当前层的节点数，每pop一次减1，while控制pop k1次，为0时表示到达当前层的最右节点，加入右视图
    2. k2表下一层的节点数，每append一次加1；
    3. 当一层结束，k1=k2，表k1变成下一层的节点数

    pass
    """
    if not root:
        return []

    res = []
    queue = deque()
    queue.append(root)
    k1 = 1
    while queue:
        k2 = 0
        while k1 != 0:
            curNode = queue.popleft()
            k1 = k1 - 1
            if curNode:
                if k1 == 0:
                    res.append(curNode.val)
                if curNode.left:
                    queue.append(curNode.left)
                    k2 = k2 + 1
                if curNode.right:
                    queue.append(curNode.right)
                    k2 = k2 + 1
        k1 = k2

    return res


def stringToTreeNode(inputValues):
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


root = stringToTreeNode([1, 2, 3, 'null', 5, 'null', 4])
print(rightSideView(root))
