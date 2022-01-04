import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

map = {}
count = 0
ans = ""
for i in range(N):
    s = input()
    c = map.get(s, 0)
    if count <= c:
        count = c
        ans = s
    map[s] = c + 1

print(ans)
