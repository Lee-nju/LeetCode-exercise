while True:
    try:
        k = int(input())
        for i in range(k):
            l = list(map(int, input().split()))
            print(sum(l[1:]))
    except:
        break
