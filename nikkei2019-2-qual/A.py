import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    ans = 0
    for i in range(1, N//2 + 1):
        if i == N - i:
            continue
        ans += 1
    print(ans)

if __name__ == "__main__":
    main()
