import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    S = ns()
    if S.count("N") and S.count("W") and S.count("S") and S.count("E"):
        print("Yes")
    elif S.count("N") and S.count("S") and S.count("W") == 0 and S.count("E") == 0:
        print("Yes")
    elif S.count("W") and S.count("E") and S.count("S") == 0 and S.count("N") == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
