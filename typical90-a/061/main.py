import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    Q = ni()
    q = deque()
    for i in range(Q):
        t, x = na()
        if t == 1:
            q.appendleft(x)
        elif t == 2:
            q.append(x)
        else:
            print(q[x - 1])

if __name__ == "__main__":
    main()
