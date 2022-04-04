import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

INF = float('inf')
LIMIT = 10 ** 6

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def judge(a, b):
    return (a * a * a) + (a * a) * b + a * (b * b) + (b * b * b) >= N

def calc(a, b):
    return (a * a * a) + (a * a) * b + a * (b * b) + (b * b * b)

N = ni()
a = 0
ans = INF
while a <= 1000000:
    left = 0
    right = 1000000
    while left <= right:
        mid = (left + right) // 2
        if judge(a, mid):
            right = mid - 1
        else:
            left = mid + 1
    ans = min(ans, calc(a, left))
    a += 1
print(ans)