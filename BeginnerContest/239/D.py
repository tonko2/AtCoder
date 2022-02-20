import math
import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def is_prime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    A, B, C, D = na()
    ans = -1
    for i in range(A, B + 1):
        flag = False
        for j in range(C, D + 1):
            if is_prime(i + j):
                flag = True
        if flag == False:
            ans = j

    if ans != -1:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main()
