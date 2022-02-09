import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin


def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    S = [None] * N
    T = [None] * N
    for i in range(N):
        S[i], T[i] = map(str, input().split())
        T[i] = int(T[i])
    X = ns()
    ans = 0
    flag = False
    for i in range(N):
        if flag:
            ans += T[i]
        else:
            if S[i] == X:
                flag = True
    print(ans)


if __name__ == "__main__":
    main()
