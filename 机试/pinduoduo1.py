numOfOne = ['4444444', '2322224', '4622226', '4424244', '2344722', '2625244', '4225444', '6622222', '4444444',
            '4445224']
dict = {}


def hash():
    for i, x in enumerate(numOfOne):
        value = 0
        for num, ch in enumerate(x):
            value += (num + 1) * int(ch)
        dict[i] = value


def count_one(nums, k):
    res = 0
    for x in nums:
        if x == 1:
            res += 1
    return str(res // k)


def judge_num(nums, k):
    if 1 not in nums[:3 * k]:
        return 8
    else:
        return 0


hash()


def pinduoduo():
    try:
        T = int(input())
        while T > 0:
            N = int(input())
            num, k = [], N // 10
            line4 = []
            for i in range(N):
                if k <= i:
                    tmp = list(map(int, input().split()))
                    if i == 4 * k:
                        line4 = tmp
                    num.append(count_one(tmp, k))
                else:
                    input()

            num = eval('+'.join(num))
            if num in numOfOne:
                res = numOfOne.index(num)
                if res == 0:
                    res = judge_num(line4, k)
                print(res)
            T -= 1
    except:
        print('出错！！')

# 2
# 10
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 1 1 1 1 0 0 0
# 0 0 1 1 0 0 1 1 0 0
# 0 0 1 1 0 0 1 1 0 0
# 0 0 0 1 1 1 1 1 0 0
# 0 0 0 0 0 0 1 1 0 0
# 0 0 0 0 0 0 1 1 0 0
# 0 0 0 1 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0
# 20
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 1 1 1 1 0 0 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 1 1 1 1 0 0 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0
# 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0
# 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

# 9
# 4
