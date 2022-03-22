N = int(input())
L = list(map(int, input().split()))

cnt = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            a, b, c = L[i], L[j], L[k]
            if a == b or b == c or a == c:
                continue
            triangle = [a, b, c]
            triangle.sort()
            if triangle[0] + triangle[1] > triangle[2]:
                cnt += 1
print(cnt)