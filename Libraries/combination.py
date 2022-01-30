def combination(n, r):
    if n < r:
        return 0
    if r == 0:
        return 1

    tmp_n = 1
    for i in range(r):
        tmp_n *= n - i
    tmp_r = 1
    for i in range(r):
        tmp_r *= r - i
    return tmp_n // tmp_r

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result