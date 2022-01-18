N = int(input())
T = ["AC", "WA", "TLE", "RE"]
C = [0] * 4

for i in range(N):
    c = input()
    C[T.index(c)] = C[T.index(c)] + 1

for i in range(4):
    print(f'{T[i]} x {C[i]}')
