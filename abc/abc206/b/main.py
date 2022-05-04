N = int(input())

d = 1
while True:
    if d * d + d - 2 * N >= 0:
        print(d)
        break
    d += 1