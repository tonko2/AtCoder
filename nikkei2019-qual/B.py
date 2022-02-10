import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = ns()
    B = ns()
    C = ns()
    ans = 0
    for i in range(N):
        ans += len({A[i], B[i], C[i]}) - 1
    print(ans)


if __name__ == "__main__":
    main()
