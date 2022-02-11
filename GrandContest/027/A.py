import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, x = na()
    A = na()
    A.sort()
    ans = 0
    for i in range(N):
        if x >= A[i]:
            x -= A[i]
            if x >= 0:
                if i == N - 1:
                    if x == 0:
                        ans += 1
                else:
                    ans += 1
    print(ans)

if __name__ == "__main__":
    main()
