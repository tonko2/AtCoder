import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = na()

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if (X[k] - X[i]) * (Y[j] - Y[i]) == (Y[k] - Y[i]) * (X[j] - X[i]):
                    continue
                ans += 1

    print(ans)

if __name__ == "__main__":
    main()
