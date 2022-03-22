S = input()
left = int(S[0:2])
right = int(S[2:])

if (left == 0 and right == 0) or (left >= 13 and right >= 13) or (left == 0 and right >= 13) or (left >= 13 and right == 0):
    print("NA")
elif 1 <= left <= 12 and 1 <= right <= 12:
    print("AMBIGUOUS")
elif 1 <= left <= 12:
    print("MMYY")
else:
    print("YYMM")