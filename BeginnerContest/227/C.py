import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    ans = 0
    for a in range(1, N + 1):
        if a * a * a > N:
            break
        for b in range(a, N + 1):
            if a * b * b > N:
                break
            c = N // a // b
            ans += c - b + 1
    print(ans)

if __name__ == "__main__":
    main()
