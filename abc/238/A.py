import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    n = ni()
    if n == 2 or n == 3 or n == 4:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
