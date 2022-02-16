import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = na()
    ans = 0

    for i in range(N):
        a = A[i] - 1
        b = A[a]
        if b == i + 1:
            ans += 1
    print(ans // 2)



if __name__ == "__main__":
    main()
