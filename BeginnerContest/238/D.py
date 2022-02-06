import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    T = ni()
    for _ in range(T):
        a, s = na()
        if s - 2 * a >= 0 and (s - 2 * a) & a == 0:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
