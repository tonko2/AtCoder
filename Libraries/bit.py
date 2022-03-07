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


def main():
    N = 5
    bit = Bit(N)
    bit.add(1, 2)
    bit.add(2, 3)
    bit.add(3, 8)
    bit.add(1, 1)
    print(bit.sum(2))
    print(bit.sum(3))

if __name__ == '__main__':
    main()