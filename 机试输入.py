import sys


def A_B2():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip()
        a = line.split()
        print(int(a[0]) + int(a[1]))


def A_B3():
    for line in sys.stdin:
        a = line.strip().split()
        if a[0] == a[1] == '0':
            break
        print(int(a[0]) + int(a[1]))


def A_B4():
    """https://ac.nowcoder.com/acm/contest/320/D"""
    for line in sys.stdin:
        a = line.strip().split()
        if a[0] == '0':
            break
        res = 0
        for x in a[1:]:
            res = res + int(x)
        print(res)


def A_B5():
    """https://ac.nowcoder.com/acm/contest/320/E"""
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        res = 0
        for x in line[1:]:
            res = res + int(x)
        print(res)


def A_B6():
    """https://ac.nowcoder.com/acm/contest/320/F"""
    for line in sys.stdin:
        a = line.strip().split()
        res = 0
        for x in a[1:]:
            res = res + int(x)
        print(res)


def A_B7():
    """https://ac.nowcoder.com/acm/contest/320/G"""
    for line in sys.stdin:
        a = line.strip().split()
        res = 0
        for x in a:
            res = res + int(x)
        print(res)


def str_sort1():
    """https://ac.nowcoder.com/acm/contest/320/H"""
    sys.stdin.readline()
    line = sys.stdin.readline().strip().split()
    line.sort()
    print(*line, sep=' ')


def str_sort2():
    """https://ac.nowcoder.com/acm/contest/320/I"""
    for line in sys.stdin:
        a = line.strip().split()
        a.sort()
        print(*a, sep=' ')


def str_sort3():
    """https://ac.nowcoder.com/acm/contest/320/J"""
    for line in sys.stdin:
        a = line.strip().split(',')
        a.sort()
        print(*a, sep=',')
