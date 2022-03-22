import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

S = ns()
X = []
i = 0
while i < len(S):
    x = "dummy"
    if len(X):
        x = X.pop()
    for j in range(len(S) - i):
        s = "".join(S[i:i+j+1])
        if s == x:
            continue
        else:
            if x != "dummy":
                X.append(x)
            X.append(s)
            i += j
            break
    i += 1
ans = len(X)
if "".join(X) != "".join(S):
    ans += 1
print(ans)