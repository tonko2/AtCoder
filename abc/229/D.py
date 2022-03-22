import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    S = ns()
    K = ni()
    A = [0] * (len(S) + 1)
    for i in range(len(S)):
        A[i + 1] = A[i] + 1 if S[i] == '.' else A[i]
    ans = 0
    right = 1
    for left in range(1, len(S) + 1):
        while right <= len(S) and A[right] - A[left-1] <= K:
            right += 1
        ans = max(ans, right - left)
    print(ans)
if __name__ == "__main__":
    main()
