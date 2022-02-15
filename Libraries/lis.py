import bisect


def lis(N, A):
    INF = float('inf')

    dp = [INF] * (N + 1)
    dp[0] = -1
    for a in A:
        index = bisect.bisect_left(dp, a)
        dp[index] = a
        print(dp)
    return bisect.bisect_left(dp, INF) - 1

def main():
    N = 5
    A = [4, 2, 3, 1, 5]
    ans = lis(N, A)
    print(ans)

if __name__ == "__main__":
    main()
