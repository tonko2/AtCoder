import itertools
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = []
    for _ in range(N):
        A.append(na())
    Q = ni()
    ng = [[False] * N for _ in range(N)]
    for _ in range(Q):
        a, b = na()
        ng[a - 1][b - 1] = True
        ng[b - 1][a - 1] = True
    P = []
    for i in range(N):
        P.append(i)

    ans = float('inf')
    for p in itertools.permutations(P):
        flag = False
        cnt = 0
        for i in range(N):
            cnt += A[i][p[i]]
        order = [0] * N
        for i in range(N):
            order[p[i]] = i
        for i in range(N - 1):
            if ng[order[i]][order[i + 1]]:
                flag = True
        if not flag:
            ans = min(ans, cnt)

    if ans == float('inf'):
        print(-1)
    else:
        print(ans)



if __name__ == "__main__":
    main()
