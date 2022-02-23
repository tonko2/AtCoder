import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()

def subtree():
    st = [(0, -1, 0)]
    val = [[X[i]] for i in range(N)]
    while st:
        v, p, t = st.pop()
        if t == 0:
            st.append((v, p, 1))
            for c in G[v]:
                if c != p:
                    st.append((c, v, 0))
        else:
            for c in G[v]:
                if c == p:
                    continue
                val[v] += val[c]
    return val

N, Q = na()
X = na()
G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = na()
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

val = subtree()
print(val)
