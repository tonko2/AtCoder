import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, B = na()
    ans = []
    if A > B:
        for i in range(1, A + 1):
            ans.append(i)
        for i in range(1, B):
            ans.append(-i)
    else:
        for i in range(1, B + 1):
            ans.append(-i)
        for i in range(1, A):
            ans.append(i)
    ans.append(-sum(ans))
    print(*ans)

if __name__ == "__main__":
    main()
