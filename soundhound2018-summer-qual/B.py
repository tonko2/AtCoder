import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    S = ns()
    w = ni()
    cut = []
    for i in range(-(-len(S) // w)):
        cut.append(S[i * w:(i + 1) * w])
    print("".join(list(zip(*cut))[0]))

if __name__ == "__main__":
    main()
