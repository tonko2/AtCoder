import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    S = ns()
    ans = []
    for i in range(len(S)):
        if S[i] == "?":
            ans.append('D')
        else:
            ans.append(S[i])

    print("".join(ans))

if __name__ == "__main__":
    main()
