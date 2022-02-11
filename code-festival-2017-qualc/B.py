import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


ans = 0
def dfs(total, n, N, arr):
    global ans
    if n == N:
        if total % 2 == 0:
            ans += 1
        return
    for x in arr[n]:
        dfs(total * x, n + 1, N, arr)


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = na()
    arr = [[] for _ in range(N)]
    for i in range(N):
        arr[i].append(A[i])
        arr[i].append(A[i] - 1)
        arr[i].append(A[i] + 1)
    dfs(1, 0, N, arr)
    print(ans)

if __name__ == "__main__":
    main()
