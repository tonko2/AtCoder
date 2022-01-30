import math

def lcm(N, A):
    res = A[0]
    for i in range(1, N):
        gcd = math.gcd(res, A[i])
        res = gcd * (res // gcd) * (A[i] // gcd)
    return res

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(lcm(N, A))