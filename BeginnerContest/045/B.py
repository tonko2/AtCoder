S = [list(input()) for _ in range(3)]
now = 0
while len(S[now]):
    tmp = now
    now = ord(S[now][0]) - ord('a')
    S[tmp] = S[tmp][1:]
print(chr(ord('A') + now))
