r, g, b = map(int, input().split())
if (100 * r + g * 10 + b) % 4 == 0:
    print("YES")
else:
    print("NO")