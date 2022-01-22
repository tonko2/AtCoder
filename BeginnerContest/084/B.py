A, B = map(int, input().split())
S = input()

if S.count("-") == 1 and S.index("-") == A:
    print("Yes")
else:
    print("No")