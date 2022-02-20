import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def rotate(S):
    return list(zip(*S[::-1]))

def find_left_top(S):
    for i in range(N):
        for j in range(N):
            if S[i][j] == '#':
                return j,i

def is_same(S, T):
    Sx, Sy = find_left_top(S)
    Tx, Ty = find_left_top(T)
    offset_x = Tx - Sx
    offset_y = Ty - Sy
    for i in range(N):
        for j in range(N):
            x = offset_x + j
            y = offset_y + i
            if 0 <= x < N and 0 <= y < N:
                if S[i][j] != T[y][x]:
                    return False
            else:
                if S[i][j] == '#':
                    return False
    return True

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
S = [ns() for _ in range(N)]
T = [ns() for _ in range(N)]

cnt_S = sum(1 for i in range(N) for j in range(N) if S[i][j] == '#')
cnt_T = sum(1 for i in range(N) for j in range(N) if T[i][j] == '#')
if cnt_S != cnt_T:
    print("No")
    exit()

for _ in range(4):
    S = rotate(S)
    if is_same(S, T):
        print("Yes")
        exit()
print("No")
