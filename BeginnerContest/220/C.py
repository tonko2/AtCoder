import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = na()
    A_sum = sum(A)
    X = ni()

    ans = (X // A_sum) * N
    X -= (X // A_sum) * A_sum

    total = 0
    for i in range(N):
        total += A[i]
        ans += 1
        if total > X:
            break
    print(ans)


if __name__ == "__main__":
    main()
