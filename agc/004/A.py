import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, B, C = na()
    ansA = abs((A // 2) * B * C - (A - A // 2) * B * C)
    ansB = abs((B // 2) * A * C - (B - B // 2) * A * C)
    ansC = abs((C // 2) * A * B - (C - C // 2) * A * B)
    print(min(ansA, ansB, ansC))

if __name__ == "__main__":
    main()
