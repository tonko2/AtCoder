import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, M = na()
    g = [[] for _ in range(N)]
    for _ in range(M):
        a, b = na()
        if b > a:
            tmp = a
            a = b
            b = tmp
        g[a - 1].append(b - 1)
    ans = 0
    for i in range(N):
        if len(g[i]) == 1:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
