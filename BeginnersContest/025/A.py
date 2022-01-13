S = list(map(str, input()))
N = int(input())

alphas = []
for i in range(0, len(S)):
    for j in range(0, len(S)):
        alphas.append(S[i] + S[j])

print(alphas[N-1])
