import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N, A, B = na()
    P, Q, R, S = na()

    for i in range(P, Q + 1):
        line = []
        for j in range(R, S + 1):
            if i - j == A - B or i + j == A + B:
                line.append('#')
            else:
                line.append('.')
        print("".join(line))

if __name__ == "__main__":
    main()
