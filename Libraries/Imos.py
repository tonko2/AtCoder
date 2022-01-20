N = 7
data = [0] * 7

l, r = 1, 3
v = 2
data[l] += v
if r+1 != N:
    data[r+1] +=-v

l, r = 3, 3
v = 3
data[l] += v
if r+1 != N:
    data[r+1] +=-v

l, r = 0, 5
v = 1
data[l] += v
if r+1 != N:
    data[r+1] +=-v

ruiseki = [0] * N  # 累積和用リスト
ruiseki[0] = data[0]
for i in range(1, N):
    ruiseki[i] = ruiseki[i-1] + data[i]

# 最終結果を出力
print(ruiseki)
# [1, 3, 3, 6, 1, 1, 0]