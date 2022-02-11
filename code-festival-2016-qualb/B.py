import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, A, B = na()
    S = ns()
    d = 0
    o = 0
    for i in range(N):
        if S[i] == 'c':
            print("No")
        elif S[i] == 'a' and d < A + B and d + o < A + B:
            print("Yes")
            d += 1
        elif S[i] == 'b' and o < B and d + o < A + B:
            print("Yes")
            o += 1
        else:
            print("No")

if __name__ == "__main__":
    main()
