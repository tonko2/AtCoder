N, S, D = map(int, input().split())
flag = False
for i in range(N):
    x, y = map(int, input().split())
    if S > x:
        if D < y:
            flag = True
if flag:
    print("Yes")
else:
    print("No")