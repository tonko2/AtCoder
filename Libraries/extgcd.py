def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b) * x
        return d, x, y
    return a, 1, 0

def main():
    a = 4
    b = 11
    print(extgcd(a, b))


if __name__ == '__main__':
    main()