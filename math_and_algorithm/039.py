import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, Q = na()
    A = [0] * (N + 1)
    for _ in range(Q):
        l, r, x = na()
        l -= 1
        r -= 1
        A[l] += x
        A[r + 1] -= x
    ans = ""
    for i in range(N - 1):
        A[i + 1] += A[i]
        if A[i] == A[i + 1]:
            ans += "="
        elif A[i] > A[i + 1]:
            ans += ">"
        else:
            ans += "<"
    print(ans)


if __name__ == "__main__":
    main()
