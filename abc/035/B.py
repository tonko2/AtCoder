S = list(input())
T = int(input())

cnt = S.count("?")
now = (0, 0)
for c in S:
    x, y = now
    if c == "U":
        y -= 1
    if c == "D":
        y += 1
    if c == "L":
        x -= 1
    if c == "R":
        x += 1
    now = (x, y)

x, y = now
ans = abs(x) + abs(y)
if T == 1:
    ans += cnt
else:
    ans -= cnt
    if ans < 0:
        if ans % 2 == 0:
            ans = 0
        else:
            ans = 1
print(ans)