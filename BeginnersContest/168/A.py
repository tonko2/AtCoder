N = int(input())

digit = N % 10
if digit == 3:
    print('bon')
elif digit in [0, 1, 6, 8]:
    print('pon')
else:
    print('hon')