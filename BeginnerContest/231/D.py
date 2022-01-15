import sys
input = lambda: sys.stdin.readline().rstrip()

sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

par = [i for i in range(N)]
def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x, y):
    return find(x) == find(y)

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y

cnt = [0] * (N + 1)

flag = True
for _ in range(M):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    cnt[A] += 1
    cnt[B] += 1
    unite(A, B)

    if cnt[A] > 2 or cnt[B] > 2:
        flag = False

if not flag:
    print('No')
    exit()

flag = dict()

for i in range(N):
    p = find(i)
    if cnt[i] < 2:
        flag[p] = True
    elif not p in flag:
        flag[p] = False
if False in flag.values():
    print('No')
else:
    print('Yes')
