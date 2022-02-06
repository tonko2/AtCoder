import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin
MOD = 998244353

def sigma(x):
    return x * (x + 1) // 2

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ns()
    ans = 0
    for i in range(len(N)):
        a = 10 ** i
        if i == len(N) - 1:
            ans = (ans + sigma(int(N) - a + 1)) % MOD
        else:
            ans = (ans + sigma(int('9' * (i + 1)) - a + 1)) % MOD

    print(ans)


if __name__ == "__main__":
    main()
