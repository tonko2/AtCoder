import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, P = na()
    A = na()
    even = 0
    odd = 0
    for a in A:
        if a % 2 == 0:
            even += 1
        else:
            odd += 1
    if even == N:
        ans = 1 << N
        if P == 0:
            print(ans)
        else:
            print(0)
    else:
        print(1 << (N - 1))

if __name__ == "__main__":
    main()
