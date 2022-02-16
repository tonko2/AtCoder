import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

MOD = 10 ** 9 + 7

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    alpha = [1] * 26
    N = int(input())
    S = input()
    for s in S:
        alpha[ord(s) - ord('a')] += 1
    ans = 1
    for a in alpha:
        ans = (ans * a)% MOD
    print(ans - 1)



if __name__ == "__main__":
    main()
