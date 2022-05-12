import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    X = ni()
    if 400 <= X <= 599:
        print(8)
    elif 600 <= X <= 799:
        print(7)
    elif 800 <= X <= 999:
        print(6)
    elif 1000 <= X <= 1199:
        print(5)
    elif 1200 <= X <= 1399:
        print(4)
    elif 1400 <= X <= 1599:
        print(3)
    elif 1600 <= X <= 1799:
        print(2)
    else:
        print(1)

if __name__ == "__main__":
    main()
