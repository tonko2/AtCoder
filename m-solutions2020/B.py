import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, B, C = na()
    K = ni()
    while K > 0:
        if C <= A:
            C *= 2
        elif C <= B:
            C *= 2
        elif B <= A:
            B *= 2
        else:
            C *= 2
        K -= 1

    if A < B < C:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
