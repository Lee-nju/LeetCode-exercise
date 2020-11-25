class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        Solution:
            利用层次遍历的方法：
            1. 对于每一层的第一个节点，看队列里有多少个点，依次拿出来
            2. 对每个当前节点，如果本层需要拿的节点还剩，next 赋值为下一个节点，否则为空
            3. 对每个当前节点，如果其右左子树，将其左子树加入队列，右子树同理。

        :param root:
        :return:
        """
        if not root:
            return
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            k = len(queue)
            while k > 0:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if k > 1:
                    node.next = queue[0]
                k -= 1

        return root
