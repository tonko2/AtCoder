import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    S = ns()
    if S.count("C") and S.count("F"):
        if S.index("C") < S.rindex("F"):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == "__main__":
    main()
