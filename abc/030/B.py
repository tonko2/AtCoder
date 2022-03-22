n, m = map(int, input().split())

a = 30 * (n % 12) + 0.5 * m
b = m * 6

if b > a:
    print(min(b - a, 360 - (b - a)))
else:
    print(min(a - b, 360 - (a - b)))
