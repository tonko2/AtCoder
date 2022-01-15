N = int(input())
M = []

for i in range(N):
    S, T = map(str, input().split())
    T = int(T)
    M.append((T, S))

M.sort(reverse=True)
print(M[1][1])