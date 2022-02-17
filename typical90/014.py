import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = na()
    A.sort()
    B = na()
    B.sort()
    ans = 0
    for i in range(N):
        ans += abs(A[i] - B[i])
    print(ans)

if __name__ == "__main__":
    main()
