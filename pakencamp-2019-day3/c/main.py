import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, M = na()
    A = []
    for i in range(N):
        A.append(na())

    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            total = 0
            for k in range(N):
                total += max(A[k][i], A[k][j])
            ans = max(ans, total)
    print(ans)



if __name__ == "__main__":
    main()
