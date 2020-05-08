from LeetCode.TreeNode import TreeNode


def isSubtree(s: TreeNode, t: TreeNode) -> bool:
    """
    Solution:
    1. 将树先序序列化为字符串str1, str2
    2. 如果str2是str1的子串，则t是s的子树
        问题：单节点：12 和 单节点：2 序列化结果为：str1=12_#_# 和 str2=2_#_#
             str1和str2是子串关系，但显然不是子树关系。
        解决：将kmp算法变形一下，即判断是否：j==len(n) 还需判断str1中匹配到的完整子串的前一个字符
        2.1 如果str1中匹配str2的子串是开头位置，那么前一个位置为-1
        2.2 如果str2中匹配str2的子串不是第一个位置，那么其一定为字符'_'

    pass
    :param s:
    :param t:
    :return:
    """
    m_str1 = []
    m_str2 = []
    serialize_tree(s, m_str1)
    serialize_tree(t, m_str2)
    str1 = '_'.join(m_str1)
    str2 = '_'.join(m_str2)
    if kmp(str1, str2):
        return True
    else:
        return False


def kmp(str1: str, str2: str) -> bool:
    next = gen_next_arr(str2)
    i = j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i = i + 1
            j = j + 1
        elif j == -1:
            i = i + 1
            j = 0
        else:
            j = next[j]

    if j == len(str2):
        # 2.1 如果str1中匹配str2的子串是开头位置，那么前一个位置为-1
        # 2.2 如果str2中匹配str2的子串不是第一个位置，那么其一定为字符'_'
        if i - len(str2) - 1 < 0 or str1[i - len(str2) - 1] == '_':
            return True
    else:
        return False


def gen_next_arr(s: str) -> [int]:
    next = [-1, 0] + [0] * (len(s) - 2)
    for i in range(2, len(s)):
        k = next[i - 1]
        while k != -1:
            if s[i - 1] == s[k]:
                next[i] = k + 1
                break
            else:
                k = next[k]
    return next


def serialize_tree(s: TreeNode, res: [str]):
    if not s:
        res.append('#')
    else:
        res.append(str(s.val))

    if s.left:
        serialize_tree(s.left, res)
    else:
        res.append('#')
    if s.right:
        serialize_tree(s.right, res)
    else:
        res.append('#')


# test kmp algorithm
# str1 = 'absniasniajs'
# str2 = 'sniasnia'
# print(kmp(str1, str2))

# test case 1
# s = TreeNode(-1).list2Tree([3,4,5,1,2,'null','null','null','null',0])
# t = TreeNode(-1).list2Tree([4,1,2])
# print(isSubtree(s, t))

# test case 2
s = TreeNode(-1).list2Tree([12])
t = TreeNode(-1).list2Tree([2])
print(isSubtree(s, t))
