import sys
import bisect

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = na()
    A.sort()
    Q = ni()
    for _ in range(Q):
        x = ni()
        index = min(bisect.bisect_left(A, x), N - 1)
        index2 = max(index - 1, 0)
        print(min(abs(x - A[index]), abs(x - A[index2])))

if __name__ == "__main__":
    main()
