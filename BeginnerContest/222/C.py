import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def isWin(c1, c2):
    if (c1 == 'G' and c2 == 'C') or (c1 == 'P' and c2 == 'G') or (c1 == 'C' and c2 == 'P'):
        return True
    else:
        return False

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, M = na()
    A = []
    for _ in range(2 * N):
        A.append(list(ns()))

    ans = []
    for i in range(2 * N):
        ans.append((0, i + 1))

    for i in range(M):
        for j in range(N):
            a, b = ans[2 * j]
            c, d = ans[2 * j + 1]
            c1 = A[b - 1][i]
            c2 = A[d - 1][i]
            if c1 == c2:
                continue
            if isWin(c1, c2):
                ans[2 * j] = (a - 1, b)
            else:
                ans[2 * j + 1] = (c - 1, d)
        ans.sort()

    for a in ans:
        print(a[1])

if __name__ == "__main__":
    main()
