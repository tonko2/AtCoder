import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    X, Y = na()
    ans = 0
    if X == 1 and Y == 1:
        ans += 400000
    ans += max(0, 300000 - (X - 1) * 100000)
    ans += max(0, 300000 - (Y - 1) * 100000)
    print(ans)

if __name__ == "__main__":
    main()
