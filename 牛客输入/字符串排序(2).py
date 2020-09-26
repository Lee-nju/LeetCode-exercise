while True:
    try:
        s = input().split()
        print(*sorted(s), sep=' ')
    except:
        break
