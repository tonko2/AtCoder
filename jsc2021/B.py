import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, M = na()
    ans = []
    A = set(na())
    B = set(na())
    for a in A:
        if a not in B:
            ans.append(a)
    for b in B:
        if b not in A:
            ans.append(b)
    ans.sort()
    print(*ans)


if __name__ == "__main__":
    main()
