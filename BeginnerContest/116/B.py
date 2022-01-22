s = int(input())
a = dict()
a[s] = 1
i = 2
while True:
    if s % 2 == 0:
        s //= 2
    else:
        s = 3 * s + 1
    x = a.get(s, 0)
    if x != 0:
        print(i)
        exit()
    a[s] = i
    i += 1