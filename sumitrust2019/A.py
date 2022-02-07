import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    M1, D1 = na()
    M2, D2 = na()
    if M1 != M2:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()
