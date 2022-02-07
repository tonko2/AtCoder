import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    H, W = na()
    for i in range(H):
        s = list(input().split(" "))
        for j in range(W):
            if s[j] == "snuke":
                h = i + 1
                w = chr(ord('A') + j)
                print(f'{w}{h}')

if __name__ == "__main__":
    main()
