N = int(input())
S = input()

ans = 0
for i in range(1, N):
    cnt = 0
    left = S[0:i]
    right = S[i:]
    left_set = set()
    for c in left:
        left_set.add(c)
    right_set = set()
    for c in right:
        if c in right_set:
            continue
        if c in left_set:
            cnt += 1
        right_set.add(c)
    ans = max(ans, cnt)

print(ans)
