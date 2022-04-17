import sys

sys.setrecursionlimit(10 ** 6)
stdin = sys.stdin

def judge(S):
    a = 0
    for c in S:
        if c == '(':
            a += 1
        else:
            a -= 1
        if a < 0:
            return False
    return a == 0




def main():
    ni = lambda: int(ns())
    na = lambda: list(map(int, stdin.readline().split()))
    ns = lambda: stdin.readline().strip()

    N = ni()
    all_str = []
    for i in range(1 << N):
        S = ""
        for j in range(N):
            if i & 1 << j:
                S += "("
            else:
                S += ")"
        if len(S) % N == 0:
            all_str.append(S)
    all_str.sort()
    ans = []
    for s in all_str:
        if judge(s):
            ans.append(s)

    for s in ans:
        print(s)

if __name__ == "__main__":
    main()
