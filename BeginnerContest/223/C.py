import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    A = [0] * N
    B = [0] * N
    half_time = 0
    for i in range(N):
        A[i], B[i] = na()
        half_time += (A[i] / B[i])

    half_time /= 2

    ans = 0
    for i in range(N):
        ans += min(A[i], half_time * B[i])
        half_time -= min(half_time, A[i] / B[i])
        if half_time == 0:
            break

    print(ans)

if __name__ == "__main__":
    main()
