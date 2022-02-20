import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = na()
    total = [0] * N
    for i in range(N - 1):
        total[i + 1] = total[i] + A[i]

    M = ni()
    B = [ni() for _ in range(M)]
    ans = 0
    for i in range(M - 1):
        l, r = B[i], B[i + 1]
        if l > r:
            l , r = r, l
        r -= 1
        ans += total[r] - total[l - 1]
    print(ans)

if __name__ == "__main__":
    main()
