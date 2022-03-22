N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_max = max(A)
B_min = min(B)

print(max(0, B_min - A_max + 1))
