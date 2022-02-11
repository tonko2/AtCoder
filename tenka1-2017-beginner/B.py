import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    ranking = []
    for i in range(N):
        a, b = na()
        ranking.append((a, b))
    ranking.sort()
    left = 1
    right = ranking[N - 1][0] + ranking[N - 1][1]
    print(right - left + 1)

if __name__ == "__main__":
    main()
