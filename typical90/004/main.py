import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    H, W = na()
    grid = []
    sum_col = [0] * H
    sum_row = [0] * W
    for i in range(H):
        grid.append(na())

    for i in range(H):
        sum_col[i] = sum(grid[i])

    for i in range(W):
        cnt = 0
        for j in range(H):
            cnt += grid[j][i]
        sum_row[i] = cnt

    ans = [[0] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            ans[i][j] = sum_col[i] + sum_row[j] - grid[i][j]

    for i in ans:
        print(*i)

if __name__ == "__main__":
    main()
