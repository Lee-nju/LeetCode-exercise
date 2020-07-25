def show_memory(unit='B', threshold=1):
    ''' 查看变量占用内存情况

    :param unit: 显示的单位，可为`B`,`KB`,`MB`,`GB`
    :param threshold: 仅显示内存数值大于等于threshold的变量
    '''
    from sys import getsizeof
    scale = {'B': 1, 'KB': 1024, 'MB': 1048576, 'GB': 1073741824}[unit]
    for i in list(globals().keys()):
        memory = eval("getsizeof({})".format(i)) // scale
        if memory >= threshold:
            print(i, memory)


def case1():
    a1 = 'h'
    a2 = 'h'
    a3 = 'h'
    a4 = 'h'
    a5 = 'h'
    a6 = 'h'
    a7 = 'h'
    a8 = 'h'
    a9 = 'h'
    a10 = 'h'
    show_memory()


if __name__ == '__main__':
    # case 1
    a1 = 'h'
    a2 = 'h3'
    a3 = 'hef'
    a4 = 'hada'
    a5 = 'hello word'
    a6 = 'hello world'
    a7 = 'h'
    a8 = 'h'
    a9 = 'h'
    a10 = 'h'
    show_memory()
    # case 2
    # a1 = 'hello'
    # a2 = 'hello'
    # a3 = 'hello'
    # a4 = 'hello'
    # a5 = 'hello'
    # a6 = 'hello'
    # a7 = 'hello'
    # a8 = 'hello'
    # a9 = 'hello'
    # a10 = 'hello'
    # show_memory()
    # case 3
    # a = [i for i in range(10000)]
    # a 85
