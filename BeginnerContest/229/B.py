A, B = map(str, input().split())
min_len = min(len(A), len(B))

for i in range(min_len):
    a = int(A[len(A) - 1 - i])
    b = int(B[len(B) - 1 - i])
    if a + b >= 10:
        print("Hard")
        exit()
print("Easy")
