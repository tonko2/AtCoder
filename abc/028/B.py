S = input()
alpha = [0] * 6
for s in S:
    index = ord(s) - ord('A')
    if index < 6:
        alpha[index] += 1
print(*alpha)