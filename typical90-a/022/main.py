import math
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    a, b, c = na()
    g = math.gcd(a, math.gcd(b, c))

    print(a // g - 1 + b // g - 1 + c // g - 1)


if __name__ == "__main__":
    main()
