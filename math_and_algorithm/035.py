import math
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    x1, y1, r1 = na()
    x2, y2, r2 = na()

    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if d == r1 + r2:
        print(4)
    elif d == abs(r1 - r2):
        print(2)
    elif d > r1 + r2:
        print(5)
    elif d > abs(r1 - r2):
        print(3)
    else:
        print(1)


if __name__ == "__main__":
    main()
