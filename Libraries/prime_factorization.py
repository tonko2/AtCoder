import math

def isPrime(x):
    '''
    素数判定

    x: num
    '''


    if x == 1 or x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def factrize(x):
    '''
    素因数分解

    x: num
    '''
    res = []
    while not isPrime(x):
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                res.append(i)
                x //= i
                break
    res.append(x)
    return res


if __name__ == '__main__':
    N = int(input())
    print(*factrize(N))