def popcount(x):
    x = x - ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x = x + (x >> 8)
    x = x + (x >> 16)
    x = x + (x >> 32)
    return x & 0x0000007f

def popcount2(x):
    return bin(x).count("1")

def main():
    print(popcount(2 ** 64 - 1))
    print(popcount2(2 ** 64 - 1))

if __name__ == '__main__':
    main()