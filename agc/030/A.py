import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, B, C = na()
    ans = min(A + B + 1, C) + B
    print(ans)

if __name__ == "__main__":
    main()
