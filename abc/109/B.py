N = int(input())
W = [input() for _ in range(N)]
s = set()
first = W[0][0]
for i, w in enumerate(W):
    if first != w[0] or w in s:
        print("No")
        exit()
    first = w[-1]
    s.add(w)
print("Yes")