S = [input() for _ in range(12)]
ans = 0
for s in S:
    if s.count("r") > 0:
        ans += 1
print(ans)