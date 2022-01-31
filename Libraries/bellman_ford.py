# O(EV)
def bellman_ford(n, s):
    d = [float('inf')] * n
    d[s] = 0
    for i in range(n):
        update = False
        for x, y, z in g:
            if d[y] > d[x] + z:
                d[y] = d[x] + z
                update = True
        if not update:
            break
    #負閉路が存在
    if i == n - 1:
        return -1
    return d

if __name__ == '__main__':
    N, M = map(int, input().split())
    H = list(map(int, input().split()))

    g = []

    for _ in range(M):
        u, v = map(int, input().split())
        Hx = H[u - 1]
        Hy = H[v - 1]
        if Hx >= Hy:
            costA = Hx - Hy
            costB = 2 * (Hy - Hx)
            g.append((u - 1, v - 1, -costA))
            g.append((v - 1, u - 1, -costB))
        else:
            costA = Hy - Hx
            costB = 2 * (Hx - Hy)
            g.append((u - 1, v - 1, -costB))
            g.append((v - 1, u - 1, -costA))

    l = bellman_ford(N, 0)
    print(-min(l))
