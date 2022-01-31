S = list(input())
S_rev = S[::-1]
if S == S_rev:
    print("Yes")
    exit()

start = 0
end = 0
for i in range(len(S)):
    if S[i] != 'a':
        end = i
        break

start_rev = 0
end_rev = 0
for i in range(len(S_rev)):
    if S_rev[i] != 'a':
        end_rev = i
        break

if end - start > end_rev - start_rev:
    print("No")
    exit()

S_rev = S_rev[end_rev:]
S = S_rev[::-1]
S = S[end:]

if S == S[::-1]:
    print("Yes")
else:
    print("No")