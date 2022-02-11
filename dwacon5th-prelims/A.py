import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = na()
    mid = sum(A) / N
    min_abs = float('inf')
    ans = 0
    for i in range(N):
        if min_abs > abs(mid - A[i]):
            min_abs = abs(mid - A[i])
            ans = i
    print(ans)

if __name__ == "__main__":
    main()
