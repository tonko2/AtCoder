S = input()
first = S.index("A")
last = S[::-1].index("Z")
print(len(S) - last - first)