import heapq

def dijkstra(edges, num_node, start):

    node = [float('inf')] * num_node
    node[start] = 0

    q = []
    heapq.heappush(q, [0, start])

    while len(q) > 0:
        _, min_point = heapq.heappop(q)

        for factor in edges[min_point]:
            goal = factor[0]
            cost = factor[1]

            if node[min_point] + cost < node[goal]:
                node[goal] = node[min_point] + cost
                heapq.heappush(q, [node[min_point] + cost, goal])

    return node

Edges = [
    [[1, 4], [2, 3]],             # ← 頂点Aからの辺のリスト
    [[2, 1], [3, 1], [4, 5]],     # ← 頂点Bからの辺のリスト
    [[5, 2]],                     # ← 頂点Cからの辺のリスト
    [[4, 3]],                     # ← 頂点Dからの辺のリスト
    [[6, 2]],                     # ← 頂点Eからの辺のリスト
    [[4, 1], [6, 4]],             # ← 頂点Fからの辺のリスト
    []                            # ← 頂点Gからの辺のリスト
]

#今の目的地の数は7つ（0~6: A~G）
node_num = 7
start = 0
opt_node = dijkstra(Edges, node_num, start)

print(opt_node)
