n = int(input())
a = list(map(int, input().split()))

alice_sum = 0
bob_sum = 0
a = sorted(a, reverse=True)

for i in range(n):
    if i % 2 == 0:
        alice_sum += a[i]
    else:
        bob_sum += a[i]

print(alice_sum - bob_sum)

'''
別解
    N = int(input())
    A = [int(i) for i in input().split()]
     
    a = sorted(A, reverse=True)
    Alice = sum(a[0::2])
    Bob = sum(a[1::2])
    print(Alice - Bob)
'''

