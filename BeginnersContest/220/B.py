K = int(input())
A, B = map(int, input().split())
a = 0
k = 1
while A != 0:
    a += (A % 10) * k
    k *= K
    A //= 10

b = 0
k = 1
while B != 0:
    b += (B % 10) * k
    k *= K
    B //= 10

print(a * b)
