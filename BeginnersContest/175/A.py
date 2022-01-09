S = input()
if S == 'RRR':
    print(3)
elif S.find('RR') != -1:
    print(2)
elif S == 'SSS':
    print(0)
else:
    print(1)