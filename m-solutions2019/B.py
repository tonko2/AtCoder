import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    S = ns()
    win = 0
    lose = 0
    for i in range(len(S)):
        if S[i] == 'o':
            win += 1
        else:
            lose += 1
    if win + 15 - len(S) >= 8:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
