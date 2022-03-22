import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, W = na()
    AB = []
    for i in range(N):
        a, b = na()
        AB.append((a, b))
    AB.sort(reverse=True)

    ans = 0

    for (a, b) in AB:
        W -= b
        ans += b * a
        if W <= 0:
            ans -= -W * a
            break
    print(ans)

if __name__ == "__main__":
    main()
