import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def digit_sum(x):
    res = 0
    while x:
        res += x % 10
        x //= 10
    return res

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    ans = float('inf')
    for i in range(1, N // 2 + 1):
        A = i
        B = N - A
        ans = min(ans, digit_sum(A) + digit_sum(B))
    print(ans)

if __name__ == "__main__":
    main()
