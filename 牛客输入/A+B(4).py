while True:
    s = input()
    if s == '0':
        break
    else:
        l = [int(x) for x in s.split()[1:]]
        print(sum(l))
