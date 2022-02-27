import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def judge():
    for i in range(N):
        for j in range(N - 5):
            cnt = 0
            for k in range(6):
                if S[i][j + k] == '#':
                    cnt += 1
            if cnt >= 4:
                return True

    for i in range(N):
        for j in range(N - 5):
            cnt = 0
            for k in range(6):
                if S[j + k][i] == '#':
                    cnt += 1
            if cnt >= 4:
                return True

    for i in range(N - 5):
        for j in range(N - 5):
            cnt = 0
            for k in range(6):
                if S[i + k][j + k] == '#':
                    cnt += 1
            if cnt >= 4:
                return True

    for i in range(N - 5):
        for j in range(N - 5):
            cnt = 0
            for k in range(6):
                if S[i + k][(N - 1) - (j + k)] == '#':
                    cnt += 1
            if cnt >= 4:
                return True
    return False
N = ni()
S = [ns() for _ in range(N)]

if judge():
    print("Yes")
else:
    print("No")
