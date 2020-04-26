from collections import deque


class Node(object):
    """节点类"""

    def __init__(self, value=-1, lChild=None, rChild=None):
        self.value = value
        self.lChild = lChild
        self.rChild = rChild


class Tree(object):
    """树类"""

    def __init__(self):
        self.root = Node()
        self.__traverse = ''

    def add(self, value):
        """不带头节点的树，按层次遍历添加新节点"""
        if self.root.value == -1:
            self.root.value = value
        else:
            node = Node(value)
            # 找到树的下一插入点的位置
            treeNode = self.nextNode()
            if not treeNode.lChild:
                treeNode.lChild = node
            elif not treeNode.rChild:
                treeNode.rChild = node

    def nextNode(self):
        """返回树的下一插入点的位置"""
        queue = deque()
        # 将根加入队列
        queue.append(self.root)
        while queue:
            # 从队列中取出第一个元素
            curNode = queue.popleft()
            if curNode.lChild:
                queue.append(curNode.lChild)
            else:
                return curNode
            if curNode.rChild:
                queue.append(curNode.rChild)
            else:
                return curNode

    def levelTraverse(self, sep=' -> '):
        """层次遍历"""
        # 置空
        self.__traverse = ''
        if self.root.value == -1:
            print('None')
        else:
            queue = deque()
            queue.append(self.root)
            while queue:
                curNode = queue.popleft()
                self.__traverse = self.__traverse + str(curNode.value) + sep
                if curNode.lChild:
                    queue.append(curNode.lChild)
                if curNode.rChild:
                    queue.append(curNode.rChild)

            print("层次遍历：" + self.__traverse[:-(len(sep))])

    def preOrderTraverse1(self, sep=' -> '):
        """
        递归先序遍历
        封装一层递归先序遍历，使得输出更加格式化，也免去了外部调用函数时需要传入root参数
        """
        if self.root.value == -1:
            print('None')
        # 置空
        self.__traverse = ''
        self.preOrderTraverse1_(self.root, sep)
        print("递归先序遍历：" + self.__traverse[:-(len(sep))])

    def preOrderTraverse1_(self, root, sep):
        """递归先序遍历的具体实现"""
        self.__traverse = self.__traverse + str(root.value) + sep
        if root.lChild:
            self.preOrderTraverse1_(root.lChild, sep)
        if root.rChild:
            self.preOrderTraverse1_(root.rChild, sep)

    def preOrderTraverse2(self, sep=' -> '):
        """非递归先序遍历"""
        if self.root.value == -1:
            print('None')
        # 置空
        self.__traverse = ''
        # 利用双端队列创建栈
        stack = deque()
        curNode = self.root
        while stack or curNode:
            while curNode:
                # 进栈的时候遍历
                self.__traverse = self.__traverse + str(curNode.value) + sep
                stack.append(curNode)
                curNode = curNode.lChild

            curNode = stack.pop().rChild

        print("非递归先序遍历：" + self.__traverse[:-(len(sep))])

    def inOrderTraverse(self, sep=' -> '):
        """非递归中序遍历"""
        if self.root.value == -1:
            print("None")

        self.__traverse = ''
        stack = deque()
        curNode = self.root
        while stack or curNode:
            while curNode:
                stack.append(curNode)
                curNode = curNode.lChild

            curNode = stack.pop()
            # 出栈的时候遍历
            self.__traverse = self.__traverse + str(curNode.value) + sep
            curNode = curNode.rChild

        print("非递归中序遍历：" + self.__traverse[:-(len(sep))])

    def postOrderTraverse(self, sep=' -> '):
        """非递归后序遍历"""
        if self.root.value == -1:
            print("None")

        self.__traverse = ''
        stack = deque()
        curNode = self.root
        while stack or curNode:
            while curNode:
                stack.append([curNode, 1])
                curNode = curNode.lChild

            if stack[-1][1] == 1:
                stack[-1][1] = 2
                curNode = stack[-1][0].rChild
            else:
                # 每个结点只有在第二次出现在栈顶时，才能访问它. 将所有出现两次的节点出栈
                while stack and stack[-1][1] == 2:
                    curNode = stack.pop()[0]
                    self.__traverse = self.__traverse + str(curNode.value) + sep
                if stack:
                    stack[-1][1] = 2
                    curNode = stack[-1][0].rChild
                else:
                    # 栈为空时，结束遍历
                    break

        print("非递归后序遍历：" + self.__traverse[:-(len(sep))])


# Test
nodeValues = [2, 4, 1, 3, 7, 9, 10, 6, 8, 5]
t = Tree()
for x in nodeValues:
    t.add(x)

# 层次遍历
t.levelTraverse()
# 指定分隔符的层次遍历
t.levelTraverse(' => ')
# 递归先序遍历
t.preOrderTraverse1()
# 非递归先序遍历
t.preOrderTraverse2()
# 非递归中序遍历
t.inOrderTraverse()
# 非递归的后序遍历
t.postOrderTraverse()
