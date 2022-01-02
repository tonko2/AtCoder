N, K = map(int, input().split())

A = [0]
total = 0

a = list(map(int, input().split()))
ans = 0
m = {0: 1}
for x in a:
    total += x
    count = m.get(total - K, 0)
    ans += count
    m[total] = m.get(total, 0) + 1
    A.append(total)

print(ans)