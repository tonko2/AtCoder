import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, A, B = na()

    if A > B:
        print(0)
    elif N == 1:
        if A == B:
            print(1)
        else:
            print(0)
    else:
        print(A + B + B * (N - 2) - (A + B + A * (N - 2)) + 1)

if __name__ == "__main__":
    main()
