import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    H = ni()
    W = ni()
    N = ni()

    print(min((-(-N // H)), -(-N // W)))

if __name__ == "__main__":
    main()
