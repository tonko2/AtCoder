import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    S = set()
    for i in range(N):
        s = ns()
        if s not in S:
            print(i + 1)
        S.add(s)

if __name__ == "__main__":
    main()
