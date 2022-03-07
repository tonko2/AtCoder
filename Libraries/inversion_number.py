class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

def inversion_number(A, N):
    res = 0
    bit = Bit(N)

    for i, p in enumerate(A):
        bit.add(p, 1)
        res += i + 1 - bit.sum(p)
    return res

def main():
    N = 10 #数列の最大値以上のサイズ
    A = [2, 1, 2]
    print(inversion_number(A, N))

if __name__ == '__main__':
    main()