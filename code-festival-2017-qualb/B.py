import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    D = na()
    M = ni()
    T = na()
    d = defaultdict(int)
    for a in D:
        d[a] += 1

    for t in T:
        if d[t] <= 0:
            print("NO")
            exit()
        else:
            d[t] -= 1
    print("YES")


if __name__ == "__main__":
    main()
