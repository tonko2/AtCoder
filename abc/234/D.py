import sys
import heapq

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, K = na()
    P = na()
    q = P[0:K]
    print(min(q))
    heapq.heapify(q)
    for i in range(K, N):
        heapq.heappush(q, P[i])
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        if a < b:
            print(b)
            heapq.heappush(q, b)
        else:
            print(a)
            heapq.heappush(q, a)

if __name__ == "__main__":
    main()
