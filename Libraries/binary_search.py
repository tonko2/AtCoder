import bisect

def main():
    A = [1, 2, 2, 2, 3]
    print(bisect.bisect_left(A, 2))   # 1
    print(bisect.bisect_left(A, 100)) # 5
    print(bisect.bisect_right(A, 2))  # 4
    print(bisect.bisect(A, 2))        # 4
    print(bisect.bisect(A, 100))      # 5

if __name__ == "__main__":
    main()
