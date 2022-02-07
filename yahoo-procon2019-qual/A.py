import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, K = na()
    if -(-N // 2) >= K:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
