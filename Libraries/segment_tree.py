class SegTree:
    """
    Segment Tree
    """

    def __init__(self, init_val, segfunc=min, ide_ele=float('inf')):
        """
        初期化

        init_val: 配列の初期値
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新

        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る

        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

def main():

    """
    最小値

    def segfunc(x, y):
        return min(x, y)
    ide_ele = float('inf')
    """

    """
    最大値
        
    def segfunc(x, y):
        return max(x, y)    
    ide_ele = -float('inf')
    """

    """
    区間和
    
    def segfunc(x, y):
        return x + y    
    ide_ele = 0
    """

    """
    区間積
   
    def segfunc(x, y):
        return x * y    
    ide_ele = 1
    """

    """
    最大公約数
   
    def segfunc(x, y):
        return math.gcd(x, y)    
    ide_ele = 0
    """

    a = [14, 5, 9, 13, 7, 12, 11, 1, 7, 8]

    seg = SegTree(a)

    """
    使い方
    
    seg = SegTree(a, segfunc=segfunc, ide_ele=ide_ele)
    """

    print(seg.query(0, 8))
    seg.update(5, 0)
    print(seg.query(0, 8))

if __name__ == '__main__':
    main()