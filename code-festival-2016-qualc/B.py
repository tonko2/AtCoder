import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    K, T = na()
    A = na()
    A.sort()
    total = sum(A[0:T - 1])
    print(max(0, A[T - 1] - total - 1))

if __name__ == "__main__":
    main()
