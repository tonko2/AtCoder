import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, K = na()
    if K == 1:
        print(0)
    else:
        print(N - K)

if __name__ == "__main__":
    main()
