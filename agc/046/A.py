import math
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    X = ni()
    d = math.gcd(360, X)
    print(360 // d)

if __name__ == "__main__":
    main()
