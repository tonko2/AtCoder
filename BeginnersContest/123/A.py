dis = []
for i in range(5):
    dis.append(int(input()))
k = int(input())

for i in range(5):
    for j in range(i+1, 5):
        if dis[j] - dis[i] > k:
            print(":(")
            exit()
print("Yay!")
