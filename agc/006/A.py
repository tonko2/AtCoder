import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    s = ns()
    t = ns()
    a = -1
    for i in range(N):
        if s[i:] == t[:N-i]:
            a = i
            break
    if a == -1:
        print(2 * N)
    else:
        print(2 * N - (N - a))

if __name__ == "__main__":
    main()
