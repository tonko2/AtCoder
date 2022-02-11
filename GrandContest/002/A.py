import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    a, b = na()
    if a <= 0 <= b:
        print("Zero")
    elif 0 < a <= b:
        print("Positive")
    else:
        if abs(b - a) % 2 == 0:
            print("Negative")
        else:
            print("Positive")

if __name__ == "__main__":
    main()
