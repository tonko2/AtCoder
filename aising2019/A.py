import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    H = ni()
    W = ni()

    print((N - H + 1) * (N - W + 1))

if __name__ == "__main__":
    main()
