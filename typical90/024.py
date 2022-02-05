import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, K = na()
    A = na()
    B = na()

    diff = 0
    for i in range(N):
        diff += abs(A[i] - B[i])
    if diff > K:
        print("No")
        exit()

    if (K % 2 == 0 and diff % 2 == 0) or (K % 2 == 1 and diff % 2 == 1):
        print("Yes")
    else:
        print("No")



if __name__ == "__main__":
    main()
