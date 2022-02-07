import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    S = ns()
    T = ns()
    if S == 'Y':
        print(T[0].upper())
    else:
        print(T[0])
if __name__ == "__main__":
    main()
