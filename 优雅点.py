import sys, time


def base_operate():
    # 1. 赋值
    a, b, c, d = 0, 1, 2, 3
    print(a, b, c, d)

    # 2. 序列解包
    ls = ['Lee', '18', 'male']
    name, age, gender = ls
    print(name, age, gender)

    # 3. if..else.. 三目运算
    x = -5
    y = x if x >= 0 else -x
    print(y)

    # 4. 判断是否为多个取值之一
    # level = 'C'
    # if level == 'A' or level == 'B' or level == 'C':
    #     print(level)
    level = 'C'
    if level in ('A', 'B', 'C'):
        print(level)

    # 5. 判断诸多条件是否至少有一个成立————不用 or，用 any
    math, physics, computer = 70, 40, 80
    if any([math < 60, physics < 60, computer < 60]):
        print('not pass!')
    else:
        print('pass!')

    # 6. 判断诸多条件是否全部成立————不用 and，用 all
    math, physics, computer = 70, 70, 80
    if all([math >= 60, physics >= 60, computer >= 60]):
        print('pass!')
    else:
        print('not pass!')

    # 7. 同时遍历序列的元素和元素下标 enumerate


# 8. 显示循环进度
def progress_bar1():
    for i in range(100):
        time.sleep(0.1)
        if (i + 1) % 10 == 0:
            sys.stdout.write('\r{}'.format(i + 1))
            sys.stdout.flush()


# 9. 显示进度条
def progress_bar2():
    for i in range(100):
        time.sleep(0.1)
        rate = float(i + 1) / 100
        rate_num = int(100 * rate)
        r = '\r[{}{}]{}%'.format('=' * rate_num, ' ' * (100 - rate_num), rate_num)
        sys.stdout.write(r)
        sys.stdout.flush()


# 10. yield 生成器
# 11. 使用装饰器给函数添加插入日志，性能测试等非核心功能
def runtime(func):
    """
    给func函数添加装饰

    :param func: 某个函数
    :return:
    """

    def warpper(*args, **kwargs):
        tic = time.time()
        result = func(*args, **kwargs)
        toc = time.time()
        print('{} is called, {} is used!'.format(func.__name__, toc - tic))
        return result

    return warpper


@runtime
def my_sum(*args):
    s = 0
    for i in args:
        s = s + i
    return s


# @runtime 只是一个语法糖，相当于 my_sum = runtime(my_sum)
print(my_sum(*range(10000)))
