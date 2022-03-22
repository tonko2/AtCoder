import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = na()
    cnt = 0
    ans = 0
    for i in range(N - 1):
        if cnt:
            cnt -= 1
            continue
        if A[i] != A[i + 1]:
            continue
        cnt = 1
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
