import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    S = ns()
    K = ni()

    C = S[K - 1]
    ans = []
    for s in S:
        if s == C:
            ans.append(C)
        else:
            ans.append("*")
    print("".join(ans))

if __name__ == "__main__":
    main()
