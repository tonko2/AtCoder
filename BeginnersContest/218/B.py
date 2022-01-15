P = list(map(int, input().split()))
A = list()
for p in P:
    A.append(chr(ord('a') + p - 1))
print("".join(A))