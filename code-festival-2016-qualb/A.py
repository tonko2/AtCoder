import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    T = list("CODEFESTIVAL2016")
    S = ns()
    ans = 0
    for i in range(len(S)):
        if T[i] != S[i]:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
