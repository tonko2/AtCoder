import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = na()
    B = na()
    C = na()

    A_cnt = [0] * 46
    B_cnt = [0] * 46
    C_cnt = [0] * 46
    for i in range(N):
       A_cnt[A[i] % 46] += 1
       B_cnt[B[i] % 46] += 1
       C_cnt[C[i] % 46] += 1

    ans = 0
    for i in range(46):
        for j in range(46):
            for k in range(46):
                if A_cnt[i] == 0 or B_cnt[j] == 0 or C_cnt[k] == 0:
                    continue
                if (i + j + k) % 46 == 0:
                    ans += A_cnt[i] * B_cnt[j] * C_cnt[k]
    print(ans)


if __name__ == "__main__":
    main()
