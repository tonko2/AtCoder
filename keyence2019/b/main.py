import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    S = ns()
    delete = len(S) - 7
    for i in range(len(S)):
        if i + delete < len(S):
            if S[0:i] + S[i + delete:] == "keyence":
                print("YES")
                exit()
    print("NO")

if __name__ == "__main__":
    main()
