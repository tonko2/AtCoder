N, A, B = map(int, input().split())
ans = 0
for _ in range(N):
    s, d = map(str, input().split())
    d = int(d)
    if s == "East":
        ans += min(max(d, A), B)
    else:
        ans -= min(max(d, A), B)
if ans == 0:
    print(ans)
elif ans < 0:
    print(f'West {-ans}')
else:
    print(f'East {ans}')