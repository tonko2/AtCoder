import queue
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    G = [[] for _ in range(N)]
    T = [0] * N
    for i in range(N):
        T[i], k, *A = na()
        for a in A:
            G[i].append(a - 1)
    print(bfs(N, G, T))

def bfs(N, G, T):
    q = queue.Queue()
    q.put(N - 1)
    used = [False] * N
    res = 0
    while not q.empty():
        n = q.get()
        if used[n]:
            continue
        used[n] = True
        res += T[n]
        for next in G[n]:
            if used[next]:
                continue
            q.put(next)
    return res

if __name__ == "__main__":
    main()
