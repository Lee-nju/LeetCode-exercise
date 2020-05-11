def myPow(x: float, n: int) -> float:
    if n == 0 and x >= 0:
        return 1

    return x ** n


print(myPow(2, 3))
print(myPow(2, -3))
