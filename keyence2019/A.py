import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    S = set(na())
    if 1 in S and 9 in S and 7 in S and 4 in S:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
