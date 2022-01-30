A, B = map(int, input().split())
A, B = min(A, B), max(A, B)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(A, B))