def combination(n, r):
    if n < r:
        return 0
    if r == 0:
        return 1

    tmp_n = 1
    for i in range(r):
        tmp_n *= n - i
    tmp_r = 1
    for i in range(r):
        tmp_r *= r - i
    return tmp_n // tmp_r

N = int(input())
A = list(map(int, input().split()))
d = dict()
for a in A:
    d[a] = d.get(a, 0) + 1
red = combination(d.get(1, 0), 2)
yellow = combination(d.get(2, 0), 2)
blue = combination(d.get(3, 0), 2)
print(red + yellow + blue)