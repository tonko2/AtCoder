cards = [[0] * 3 for _ in range(3)]

def isBingo():
    for i in range(3):
        flag = True
        for j in range(3):
            if cards[i][j] == 0:
                flag = False
        if flag:
            return flag

    for i in range(3):
        flag = True
        for j in range(3):
            if cards[j][i] == 0:
                flag = False
        if flag:
            return flag

    if cards[0][0] == 1 and cards[1][1] == 1 and cards[2][2] == 1:
        return True

    if cards[0][2] == 1 and cards[1][1] == 1 and cards[2][0] == 1:
        return True

    return False

d = dict()
for i in range(3):
    A = list(map(int, input().split()))
    for j, a in enumerate(A):
        d[a] = (i, j)

N = int(input())
for i in range(N):
    num = int(input())
    y, x = d.get(num, (-1, -1))

    if x != -1:
        cards[y][x] = 1

if isBingo():
    print("Yes")
else:
    print("No")
