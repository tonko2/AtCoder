import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin



ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

N = ni()
A, B, C = na()
ans = float('inf')
for i in range(0, 10000):
    for j in range(0, 10000):
        total = i * A + j * B
        if total > N:
            break
        if i + j > 10000:
            break
        if ans < i + j:
            break
        if (N - total) % C == 0:
            if i + j + (N - total) // C < 10000:
                ans = min(ans, i + j + (N - total) // C)
print(ans)

