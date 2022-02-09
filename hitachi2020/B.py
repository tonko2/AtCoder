import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, B, M = na()
    a = na()
    b = na()
    ans = float('inf')
    for i in range(M):
        x, y, c = na()
        ans = min(ans, a[x-1] + b[y-1] - c)
    a.sort()
    b.sort()
    print(min(ans, a[0] + b[0]))

if __name__ == "__main__":
    main()
