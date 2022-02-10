import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    d = defaultdict(int)
    for _ in range(3):
        a, b = na()
        d[a] += 1
        d[b] += 1

    if len(d.keys()) == 4 and sum(d.values()) == 6 and max(d.values()) == 2 and min(d.values()) == 1:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
