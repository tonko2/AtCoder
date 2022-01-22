S = set(list(map(str, input())))
for i in range(0, 26):
    if chr(ord('a') + i) not in S:
        print(chr(ord('a') + i))
        exit()
print("None")