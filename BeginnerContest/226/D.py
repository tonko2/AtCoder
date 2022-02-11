import math
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    city = [None] * N
    for i in range(N):
        x, y = na()
        city[i] = (x, y)

    S = set()
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            x1, y1 = city[i]
            x2, y2 = city[j]
            d = math.gcd(x2 - x1, y2 - y1)
            S.add(((x2 - x1) // d, (y2 - y1) // d))
    print(len(S))


if __name__ == "__main__":
    main()
