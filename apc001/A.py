import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    X, Y = na()
    if X % Y == 0:
        print(-1)
    else:
        print(X)

if __name__ == "__main__":
    main()
