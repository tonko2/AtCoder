def calc(x):
    if x == 0:
        return 1
    else:
        return x * calc(x - 1)
coins = [calc(i + 1) for i in range(13)]

P = int(input())

ans = 0
for i in range(len(coins)):
    if P >= coins[-1 - i]:
        ans += P // coins[-1 - i]
        P %= coins[-1 - i]

print(ans)
