def eratosthenes(N):
    prime = [ True ] * (N + 1)
    LIMIT = int(N ** 0.5)
    for i in range(2, LIMIT + 1):
        if prime[i] == True:
            for j in range(2 * i, N + 1, i):
                prime[j] = False
    return prime

def main():
    N = int(input())
    prime = eratosthenes(N)

    for i in range(2, N + 1):
        if prime[i] == True:
            print(i)

if __name__ == '__main__':
    main()
