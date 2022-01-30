import math

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

bc = (cx - bx, cy - by)
ba = (ax - bx, ay - by)
ca = (ax - cx, ay - cy)
cb = (bx - cx, by - cy)

if bc[0] * ba[0] + bc[1] * ba[1] < 0:
    print(math.sqrt(ba[0] ** 2 + ba[1] ** 2))
elif cb[0] * ca[0] + cb[1] * ca[1] < 0:
    print(math.sqrt(ca[0] ** 2 + ca[1] ** 2))
else:
    S = abs(ba[0] * bc[1] - ba[1] * bc[0])
    bc_len = math.sqrt(bc[0] ** 2 + bc[1] ** 2)
    print(S / bc_len)
