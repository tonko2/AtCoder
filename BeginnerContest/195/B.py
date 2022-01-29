A, B, W = map(int, input().split())
W *= 1000

ans_min = 1001
ans_max = -1
for i in range(0, 1000001):
    hoge = (W - A * i) // B
    if A * i <= W:
        print(f'i = {i}, A * i = {A * i}, B * i = {B * i}')
        ans_min = min(ans_min, i + hoge)
        ans_max = max(ans_max, i + hoge)

if ans_max == -1:
    print("UNSATISFIABLE")
else:
    print(f'{ans_min} {ans_max}')