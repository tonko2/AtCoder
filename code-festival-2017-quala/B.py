import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, M, K = na()
    for i in range(0, N + 1):
        for j in range(0, M + 1):
            if i * (M - j) + j * (N - i) == K:
                print("Yes")
                exit()
    print("No")

if __name__ == "__main__":
    main()
