import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    X = ns()
    alpha_to_custom = defaultdict()
    custom_to_alpha = defaultdict()
    for i in range(26):
        alpha_to_custom[chr(ord('a') + i)] = X[i]
        custom_to_alpha[X[i]] = chr(ord('a') + i)


    N = ni()
    ans = []
    for i in range(N):
        s = ns()
        converted_s = []
        for c in s:
            converted_s.append(custom_to_alpha[c])
        ans.append("".join(converted_s))
    ans.sort()
    for s in ans:
        converted_s = []
        for c in s:
            converted_s.append(alpha_to_custom[c])
        print("".join(converted_s))


if __name__ == "__main__":
    main()
