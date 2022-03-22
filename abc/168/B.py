K = int(input())
S = input()
ex = ""
if K < len(S):
    ex = "..."
print(S[0:K] + ex)