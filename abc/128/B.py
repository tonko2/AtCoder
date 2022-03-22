N = int(input())
restaurant = []
for i in range(N):
    city, point = map(str, input().split())
    restaurant.append((city, -int(point), i + 1))

restaurant = sorted(restaurant)

for i in range(N):
    city, point, index = restaurant[i]
    print(index)
