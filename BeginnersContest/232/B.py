def move_str(str, n):
    res = ""
    for c in str:
        res += chr(ord('a') + (ord(c) - ord('a') + n) % 26)
    return res

S1 = input()
S2 = input()

for i in range(26):
    if move_str(S1, i) == S2:
        print('Yes')
        exit()
print('No')

