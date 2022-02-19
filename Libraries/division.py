def modpow(a, b, m):
    p = a, res = 1
    for i in range(30):
        if b & (1 << i) != 0:
            res *= p
            res %= p
        p *= p
        p %= m
    return res

# a
def division(a, b, m):
    return ()