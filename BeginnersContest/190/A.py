A, B, C = map(int, input().split())

if C == 0:
    B -= A
    A -= A
    if B < 0:
        print('Takahashi')
    else:
        print('Aoki')
else:
    A -= B
    B -= B
    if A < 0:
        print('Aoki')
    else:
        print('Takahashi')
