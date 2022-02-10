import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = na()
    cum_sum = [0] * N
    cum_sum[0] = A[0]
    total = sum(A)
    ans = float('inf')
    for i in range(1, N - 1):
        cum_sum[i] = cum_sum[i - 1] + A[i]
    for a in cum_sum:
        ans = min(ans, abs(a - (total - a)))

    print(ans)


if __name__ == "__main__":
    main()
