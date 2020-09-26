while True:
    try:
        k = int(input())
        for i in range(k):
            a, b = map(int, input().split())
            print(a + b)
    except:
        break
