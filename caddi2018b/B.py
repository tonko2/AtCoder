import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, H, W = na()
    ans = 0
    for _ in range(N):
        a, b = na()
        if a >= H and b >= W:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
