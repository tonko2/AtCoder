import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = na()
    avg = -(-sum(A) // N)
    avg2 = sum(A) // N
    ans = 0
    ans2 = 0
    for a in A:
        ans += (a - avg) ** 2
        ans2 += (a - avg2) ** 2
    print(min(ans, ans2))


if __name__ == "__main__":
    main()
