import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    C = na()
    total = sum(C)
    for i in range(1 << 4):
        cnt = 0
        for j in range(4):
            if i & (1 << j):
               cnt += C[j]
        if cnt == total - cnt:
            print("Yes")
            exit()


    print("No")

if __name__ == "__main__":
    main()
