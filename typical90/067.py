import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def base_10_to_n(x, n):
    res = []
    while x:
        res.append(str(x % n))
        x //= n
    res.reverse()
    return "".join(res)

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, K = map(str, input().split())
    if N == '0':
        print(0)
        exit()
    N_10 = int(N, 8)
    N_9 = ''
    for i in range(int(K)):
        N_9 = base_10_to_n(N_10, 9)
        N_9 = N_9.replace("8", "5")
        N_10 = int(N_9, 8)
    print(N_9)


if __name__ == "__main__":
    main()
