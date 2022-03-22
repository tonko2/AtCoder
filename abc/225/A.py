import itertools

S = list(input())
cnt = dict()
for v in itertools.permutations(S):
    cnt[v] = 1

print(len(cnt))
