import queue

a, N = map(int, input().split())

Q = queue.Queue()
Q.put((1, 0))

ans = 0
S = set()
while not Q.empty():
    x, c = Q.get()

    if x in S:
        continue
    S.add(x)
    if x == N:
        print(c)
        exit()

    if x  > N * 2:
        continue

    Q.put((x * a, c + 1))
    if x >= 10 and x % 10 != 0:
        x_str = str(x)
        next = int(x_str[-1] + x_str[0:len(x_str) - 1])
        Q.put((next, c + 1))

print(-1)