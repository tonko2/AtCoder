S = list(map(str, input()))
S.sort()

T = list(map(str, input()))
T.sort(reverse=True)

if "".join(S) < "".join(T):
    print("Yes")
else:
    print("No")
