import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, Q = na()
    A = na()
    total = [0] * (N + 1)
    for i in range(0, N):
        total[i + 1] = total[i] + A[i]

    for _ in range(Q):
        l, r = na()
        print(total[r] - total[l - 1])

if __name__ == "__main__":
    main()
