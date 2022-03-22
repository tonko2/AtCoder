L, R = map(int, input().split())
L -= 1
R -= 1
S = input()

print(S[:L] + ''.join(reversed(S[L:R+1])) + S[R+1:len(S)])