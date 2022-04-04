import bisect

def main():
    A = [1, 2, 2, 2, 3]
    print(bisect.bisect_left(A, 2))   # 1
    print(bisect.bisect_left(A, 100)) # 5
    print(bisect.bisect_right(A, 2))  # 4
    print(bisect.bisect(A, 2))        # 4
    print(bisect.bisect(A, 100))      # 5


    def judge(x):
        return True

    LIMIT = 10000
    left = 0
    right = LIMIT
    while left <= right:
        mid = (left + right) // 2
        if judge(mid):
            right = mid - 1
        else:
            left = mid + 1

if __name__ == "__main__":
    main()
