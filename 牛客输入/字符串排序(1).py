while True:
    try:
        k = input()
        s = input().split()
        print(*sorted(s), sep=' ')
    except:
        break
