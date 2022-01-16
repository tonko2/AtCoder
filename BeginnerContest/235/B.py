N = int(input())
H = list(map(int, input().split()))

f = H[0]
for i in range(N - 1):
    if H[i] < H[i + 1]:
        f = H[i + 1]
    else:
        break
print(f)