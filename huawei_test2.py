import sys


def test2(M: str, k: int) -> str:
    res = M
    while k > 0:
        n = len(res)
        i = 0
        while i < n - 1:
            if res[i] > res[i + 1]:
                break
            i = i + 1
        res = res[0:i] + res[i + 1:n]
        k = k - 1

    return res


if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    k = int(sys.stdin.readline().strip())
    if not line:
        print(0)
    print(test2(line, k))
