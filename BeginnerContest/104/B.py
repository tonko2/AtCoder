S = input()
flag1 = True
flag2 = True
flag3 = True

flag1 = S[0] == "A" and S.count("A") == 1
flag2 = S.count("C") == 1 and 2 <= S.index("C") <= len(S)-2
S = S.replace("A", "")
S = S.replace("C", "")
flag3 = S.islower()

if all([flag1, flag2, flag3]):
    print("AC")
else:
    print("WA")