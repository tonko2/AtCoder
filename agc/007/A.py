import queue
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def bfs(H, W, field):
    q = queue.Queue()
    q.put((0, 0))
    used = [[False] * W for _ in range(H)]
    while not q.empty():
        x, y = q.get()
        used[y][x] = True
        if x == W - 1 and y == H - 1:

            for i in range(H):
                for j in range(W):
                    if field[i][j] == '#' and used[i][j] == False:
                        print("Impossible")
                        exit()
            print("Possible")
            exit()

        dx = [0, 1]
        dy = [1, 0]
        cnt = 0
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < W and ny < H and field[ny][nx] == '#':
                cnt += 1
                q.put((nx, ny))
        if cnt == 2:
            break

    print("Impossible")

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    H, W = na()
    field = []
    for _ in range(H):
        field.append(ns())
    if field[0][0] == '.' or field[H - 1][W - 1] == '.':
        print("Impossible")
        exit()
    bfs(H, W, field)

if __name__ == "__main__":
    main()
