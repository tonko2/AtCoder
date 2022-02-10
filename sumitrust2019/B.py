import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    for i in range(N + 1):
        if int(i * 1.08) == N:
            print(i)
            exit()
    print(':(')

if __name__ == "__main__":
    main()
