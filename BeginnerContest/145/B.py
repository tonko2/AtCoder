N = int(input())
S = input()

if N % 2 != 0:
    print("No")
else:    
    if S[0:len(S)//2] == S[len(S)//2:]:
        print("Yes")
    else:
        print("No")