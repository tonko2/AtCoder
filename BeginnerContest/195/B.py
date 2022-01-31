import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, B, W = na()
    W *= 1000
    ans_min = float('inf')
    ans_max = -1
    for i in range(1, 1000 * 1000 + 1):
        if A * i <= W <= B * i:
            ans_max = max(ans_max, i)
            ans_min = min(ans_min, i)

    if ans_max == -1:
        print("UNSATISFIABLE")
    else:
        print(ans_min, ans_max)


if __name__ == "__main__":
    main()
