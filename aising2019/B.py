import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A, B = na()
    set_A = 0
    set_B = 0
    set_C = 0
    P = na()
    for p in P:
        if p <= A:
            set_A += 1
        elif p >= B + 1:
            set_C += 1
        else:
            set_B += 1
    print(min(set_A, set_B, set_C))

if __name__ == "__main__":
    main()
