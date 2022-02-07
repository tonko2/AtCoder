import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    H1, M1, H2, M2, K = na()
    print(H2 * 60 + M2 - (H1 * 60 + M1 + K))

if __name__ == "__main__":
    main()
