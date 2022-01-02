strs = ['dreameraser', 'dreamerase', 'dreamer', 'dream', 'eraser', 'erase']

S = input()

while True:
    prev = S
    for str in strs:
        if S.find(str) == 0:
            S = S.replace(str, '', 1)
            break
    if prev == S:
        break

if S == '':
    print('YES')
else:
    print('NO')

'''
別解
    s=input()
    while(s):
      if(s[-7:]=="dreamer"):
        s=s[:-7]
      elif(s[-5:]=="dream"):
        s=s[:-5]
      elif(s[-6:]=="eraser"):
        s=s[:-6]
      elif(s[-5:]=="erase"):
        s=s[:-5]
      else:
        print("NO")
        exit()
    print("YES")
'''



