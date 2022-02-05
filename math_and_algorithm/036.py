import math
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, B, H, M = na()

    alpha = 30 * H + 0.5 * M
    beta = 6 * M
    rad = math.radians((alpha - beta))
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(rad)))


if __name__ == "__main__":
    main()
