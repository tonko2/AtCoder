S = []
for i in range(3):
    S.append(input())

T = list(map(str, input()))

ans = ""
for i in range(len(T)):
    ans += S[(ord(T[i]) - ord('0')) - 1]

print(ans)