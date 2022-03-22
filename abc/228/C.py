import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, K = na()
    P = []
    sorted_P = []
    for i in range(N):
        total = sum(na())
        P.append(total)
        sorted_P.append((total, i + 1))

    sorted_P.sort(reverse=True)
    (base, _) = sorted_P[K - 1]

    for p in P:
        if min(1200, p + 300) >= base:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
