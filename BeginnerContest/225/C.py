import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, M = na()
    grid = []
    for _ in range(N):
        grid.append(na())

    # 横チェック
    for i in range(N):
        for j in range(M - 1):
            if grid[i][j + 1] - grid[i][j] == 1:
                continue
            print("No")
            exit()

    # 縦チェック
    for i in range(M):
        for j in range(N - 1):
            if grid[j + 1][i] - grid[j][i] == 7:
                continue
            print("No")
            exit()

    # 7の倍数が最後かどうか
    for i in range(N):
        for j in range(M):
            if grid[i][j] % 7 == 0:
                if j != M - 1:
                    print("No")
                    exit()

    print("Yes")

if __name__ == "__main__":
    main()
