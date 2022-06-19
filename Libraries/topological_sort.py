# ・ノードIDは、0～N-1とする
# ・以下のデータは既に作られているとする
#   inc[n] = nに流入するリンク数(int)
#   out[n] = nからの流出先のノード集合(list or set)

# N = 7
# inc = [0] * N
# inc[0] = 3
# inc[1] = 0
# inc[2] = 0
# inc[3] = 0
# inc[4] = 1
# inc[5] = 1
# inc[6] = 1

# out = [[] for _ in range(N)]
# out[0] = [4, 5, 6]
# out[1] = [0]
# out[2] = [0]
# out[3]= [0]
# out[4] = []
# out[5] = []
# out[6] = []
import heapq

def topological_sort(inc, out):
    # 入次数が0のノード
    q = [i for i, c in enumerate(inc) if c == 0]
    res = []
    while q:
        v = heapq.heappop(q)
        res.append(v)
        for j in out[v]:
            inc[j] -= 1
            if inc[j] == 0:
                heapq.heappush(q, j)
    return res