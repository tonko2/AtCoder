N = int(input())
S = list(str(N))
S_num_sum = sum(list(map(int, S)))

if N % S_num_sum == 0:
    print("Yes")
else:
    print("No")
