V = ['a', 'i', 'u', 'e', 'o']
W = list(input())
ans = ""
for w in W:
    if w in V:
        continue
    ans += w
print(ans)
