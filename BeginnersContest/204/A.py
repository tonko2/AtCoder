x, y = map(int, input().split())

if x == y:
    print(x)
else:
    hands = [0, 1, 2]
    hands.remove(x)
    hands.remove(y)
    print(hands[0])