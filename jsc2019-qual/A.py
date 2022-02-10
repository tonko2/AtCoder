import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    M, D = na()
    ans = 0
    for m in range(1, M + 1):
        if m < 2:
            continue
        for d in range(1, D + 1):
            if d < 10:
                continue
            if d % 10 < 2 or int(d // 10) < 2:
                continue
            if m == (d % 10) * int(d // 10):
                ans += 1
    print(ans)

if __name__ == "__main__":
    main()
