import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, V = na()
    B, W = na()
    T = ni()

    if max(0, T * (V - W)) >= abs(A - B):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
