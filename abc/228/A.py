S, T, X = map(int, input().split())

if S == 0:
    S = 24

if T == 0:
    T = 24

if S <= T:
    if S <= X < T:
        print('Yes')
    else:
        print('No')
else:
    if S <= X <= 24 or 0 <= X < T:
        print('Yes')
    else:
        print('No')