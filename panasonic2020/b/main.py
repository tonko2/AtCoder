import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    H, W = na()
    if H == 1 or W == 1:
        print(1)
    else:
        print(-(-H // 2) * (-(-W // 2)) + (H // 2) * (W // 2))

if __name__ == "__main__":
    main()
