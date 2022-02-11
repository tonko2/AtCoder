import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    L = na()
    L.sort()
    ans = 0
    i = 0
    while i < 2 * N:
        ans += min(L[i], L[i + 1])
        i += 2
    print(ans)


if __name__ == "__main__":
    main()
