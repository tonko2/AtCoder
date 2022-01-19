N, A, B = map(int, input().split())

if N <= A + B:
    print(min(N, A))
else:
    ans = (N // (A + B)) * A + min((N % (A + B), A))
    print(ans)