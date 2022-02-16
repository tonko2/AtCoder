class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


def kruskal(N, g):
    edges = []

    for u in range(1, N + 1):
        for (v, c) in g[u]:
            edges.append((c, u, v))
    edges.sort()

    uf = UnionFind(N + 1)
    res = 0
    for (c, u, v) in edges:
        if uf.same(u, v):
            continue
        res += c
        uf.union(u, v)
    return res

def main():
    N, M = map(int, input().split())
    g = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, c = map(int, input().split())
        g[u].append((v, c))
    ans = kruskal(N, g)
    print(ans)

# 入力
# 4 5
# 1 2 2
# 1 3 8
# 1 4 10
# 2 3 2
# 3 4 2

if __name__ == '__main__':
    main()

