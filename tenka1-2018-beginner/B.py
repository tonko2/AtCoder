import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, B, K = na()
    for i in range(K):
        if i % 2 == 0:
            if A % 2 != 0:
                A = (A - 1)
            A //= 2
            B += A
        else:
            if B % 2 != 0:
                B = (B - 1)
            B //= 2
            A += B
    print(A, B)

if __name__ == "__main__":
    main()
