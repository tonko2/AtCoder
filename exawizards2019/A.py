import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, B, C = na()
    if A == B and B == C:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
