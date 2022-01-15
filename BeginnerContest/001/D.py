# 実装は合ってるが、TLEで通らない

def show(start, end):
    start = str(start).zfill(4)
    end = str(end).zfill(4)
    print(f'{start}-{end}')

duration = 2402 * [0]
start = -1

N = int(input())
for i in range(N):
    s, e = input().split('-')
    s = int(s)
    e = int(e)

    if s % 10 == 0:
        pass
    elif s % 10 < 5:
        s -= s % 10
    elif s % 10 > 5:
        s -= s % 10 - 5

    if e % 10 == 0:
        pass
    elif e % 10 < 5:
        e += 5 - e % 10
    elif e % 10 > 5:
        e += 10 - e % 10

    if e % 100 == 60:
        e += 40

    for j in range(s, e+1):
        duration[j] += 1

for i in range(len(duration)):
    if duration[i] > 0 and start == -1:
        start = i
    if duration[i] == 0 and start != -1:
        show(start, i-1)
        start = -1

'''
別解
N = int(input())
S, E = [], []
for i in range(N):
    s, e = map(int, input().split("-"))
    s -= s % 5
    e += (5 - e % 5) % 5
    if e % 100 == 60:
        e += 40
    S.append(s)
    E.append(e)

S.sort()
E.sort()

S.append(2401)

start = S[0]
for i in range(len(E)):
    if E[i] < S[i + 1]:
        end = E[i]
        print("%04d-%04d" % (start, end))
        start = S[i + 1]
'''