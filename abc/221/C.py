import itertools
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    S = list(ns())
    S.sort()
    ans = 0
    S_len = len(S)
    for p in itertools.permutations(S):
        for i in range(S_len - 1):
            a = int("".join(p[0:i + 1]))
            b = int("".join(p[i + 1:]))
            ans = max(ans, a * b)

    print(ans)


if __name__ == "__main__":
    main()
