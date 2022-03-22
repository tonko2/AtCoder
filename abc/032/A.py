def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input())
b = int(input())
n = int(input())

a, b = max(a, b), min(a, b)
c = a * b // gcd(a, b)
d = c
while c < n:
    c += d

print(c)
