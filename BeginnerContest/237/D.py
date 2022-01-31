from collections import deque

N = int(input())
S = list(input())
ans = deque([N])
for i in range(N)[::-1]:
    if S[i] == 'R':
        ans.appendleft(i)
    else:
        ans.append(i)
print(*ans)