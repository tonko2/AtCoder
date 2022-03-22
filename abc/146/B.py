N = int(input())
S = list(map(str, input()))

for i, c in enumerate(S):
    next = chr(ord('A') + ((ord(c) - ord('A') + N) % 26))
    S[i] = next

print("".join(S))
