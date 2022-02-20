import sys
import math

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    x1, y1, x2, y2 = na()
    dx = [1, 1, 2, 2, -1, -1, -2, -2]
    dy = [2, -2, 1, -1, 2, -2, 1, -1]
    for i in range(8):
        px = x1 + dx[i]
        py = y1 + dy[i]
        if abs(x1 - px) ** 2 + abs(y1 - py) ** 2 == abs(x2 - px) ** 2 + abs(y2 - py) ** 2:
            if abs(x1 - px) ** 2 + abs(y1 - py) ** 2 == 5:
                print("Yes")
                exit()
    print("No")


if __name__ == "__main__":
    main()
