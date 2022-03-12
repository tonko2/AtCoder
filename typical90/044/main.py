import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, Q = na()
    A = na()
    change = 0
    for i in range(Q):
        t, x, y = na()
        if t == 1:
            x = (x + change) % N
            y = (y + change) % N
            A[x - 1], A[y - 1] = A[y - 1], A[x - 1]
        elif t == 2:
            change = (change - 1) % N
        else:
            print(A[(change + x - 1) % N])


if __name__ == "__main__":
    main()
