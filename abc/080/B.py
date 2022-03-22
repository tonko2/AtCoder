N = int(input())
digits = sum(list(map(int, str(N))))
if N % digits == 0:
    print("Yes")
else:
    print("No")
