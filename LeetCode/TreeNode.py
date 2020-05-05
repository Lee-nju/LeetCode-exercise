from _collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = TreeNode(-1)

    def list2Tree(self, l: [int]):
        """
        将list=[5,1,4,null,null,3,6] 转成树节点的格式

        :param l:
        :return:
        """
        self.root = TreeNode(l[0])
        i, queue = 1, deque()
        queue.append(self.root)
        while queue:
            k = len(queue)
            for j in range(k):
                node = queue.popleft()
                if i == len(l):
                    continue
                if l[i] != 'null':
                    node.left = TreeNode(l[i])
                    queue.append(node.left)
                i = i + 1
                if l[i] != 'null':
                    node.right = TreeNode(l[i])
                    queue.append(node.right)
                i = i + 1
        return self

    def print_tree(self):
        """层次遍历输出"""
        if self.root.val == -1:
            return
        queue = deque()
        queue.append(self.root)
        m_list = []
        while queue:
            node = queue.popleft()
            m_list.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append((node.right))

        print(m_list)


l = [5, 1, 4, 'null', 'null', 3, 6, 7, 'null', 1, 'null', 'null', 'null', 'null', 'null']
m_tree = Tree().list2Tree(l)
m_tree.print_tree()
