while True:
    try:
        l = list(map(int, input().split()))
        print(sum(l))
    except:
        break
