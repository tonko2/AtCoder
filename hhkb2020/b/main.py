import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    H, W = na()
    field = []
    for _ in range(H):
        field.append(ns())

    ans = 0
    for i in range(H):
        for j in range(W):
            if field[i][j] == '#':
                continue
            if i + 1 < H and field[i + 1][j] == '.':
                ans += 1
            if j + 1 < W and field[i][j + 1] == '.':
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
