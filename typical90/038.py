import sys
import math

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def lcm(N, A):
    res = A[0]
    for i in range(1, N):
        gcd = math.gcd(res, A[i])
        res = gcd * (res // gcd) * (A[i] // gcd)
    return res

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, B = na()
    ans = lcm(2, [A, B])
    if ans > 10 ** 18:
        print("Large")
    else:
        print(ans)

if __name__ == "__main__":
    main()
