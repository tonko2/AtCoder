N, K, M = map(int, input().split())

total = sum(list(map(int, input().split())))

if M * N - total <= K:
    print(max(0, M * N - total))
else:
    print(-1)