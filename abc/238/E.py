import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, Q = na()
    A = [0] * N
    total = [0] * N

    for i in range(Q):
        l, r = na()
        l -= 1
        r -= 1
        A[l] += 1
        if r + 1 != N:
            A[r + 1] += -1

    total[0] = A[0]


    for i in range(1, N):
        total[i] = total[i - 1] + A[i]

    for i in range(0, N):
        if total[i] == 0:
            print("No")
            exit()

    cnt = 0
    for i in range(0, N):
        if total[i] % 2 != 0:
            cnt += 1

    if cnt % 2 == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
