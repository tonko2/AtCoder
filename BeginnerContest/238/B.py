import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    n = ni()
    A = na()
    pi = [0] * 360
    now = 0
    for a in A:
        now = (now + a) % 360
        pi[now] = 1

    index = []
    for i in range(0, 360):
        if pi[i] == 1:
            index.append(i)

    ans = max(360 - index[len(index) - 1], index[0])

    for i in range(0, len(index) - 1):
        ans = max(ans, index[i + 1] - index[i])

    print(ans)









if __name__ == "__main__":
    main()
