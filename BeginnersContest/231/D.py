import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

hashmap = {}
ok = True
for _ in range(M):
    A, B = map(int, input().split())
    a = hashmap.get(A, 0)
    b = hashmap.get(B, 0)
    hashmap[A] = a + 1
    hashmap[B] = b + 1

    if a == 1:
        hashmap[B] = 2
    if b == 1:
        hashmap[A] = 2

    if a > 1 or b > 1:
        ok = False

print("Yes" if ok else "No")