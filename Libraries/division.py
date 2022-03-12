def modpow(a, b, m):
    p = a, res = 1
    for i in range(30):
        if b & (1 << i) != 0:
            res *= p
            res %= p
        p *= p
        p %= m
    return res

# a / b % m を返す関数
def division(a, b, m):
    return (a * modpow(b, m - 2, m)) % m