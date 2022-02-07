import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    a, b = na()
    if a + b == 15:
        print('+')
    elif a * b == 15:
        print('*')
    else:
        print('x')

if __name__ == "__main__":
    main()
