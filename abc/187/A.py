A, B = map(str, input().split())
print(max(sum(map(int, str(A))), sum(map(int, str(B)))))