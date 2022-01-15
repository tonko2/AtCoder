A, B, C, D = map(int, input().split())

if A / B == C / D:
    print("DRAW")
elif A / B < C / D:
    print("TAKAHASHI")
else:
    print("AOKI")