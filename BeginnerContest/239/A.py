import sys
import math

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    x= ni()
    print(math.sqrt(x * (12800000 + x)))

if __name__ == "__main__":
    main()
