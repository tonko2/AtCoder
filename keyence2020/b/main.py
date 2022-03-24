import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    XL = []
    for _ in range(N):
        x, l = na()
        XL.append((x + l, x - l))
    XL.sort()
    left = -float('inf')
    ans = N
    for r, l in XL:
        if left <= l:
            left = r
        else:
            ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
