import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, D, H = na()
    ans = 0
    for i in range(N):
        d, h = na()
        a = (H - h) / (d - D)
        b = D * a + H
        ans = max(ans, b)
    print(ans)


if __name__ == "__main__":
    main()
