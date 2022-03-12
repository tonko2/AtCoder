import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    H, W = na()
    if H == 1 or W == 1:
        print(max(H, W))
    else:
        print(((H + 1) // 2) * ((W + 1) // 2))

if __name__ == "__main__":
    main()
