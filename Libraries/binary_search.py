import bisect

def main():

    # bisect_left(A, x)は、Aのx未満の要素の個数
    # bisect_right(A, x)は、Aのx以下の要素の個数
    A = [1, 6, 8, 9, 14]
    print(bisect.bisect_left(A, 6))  # 1
    print(bisect.bisect_right(A, 6)) # 2
    print(bisect.bisect_left(A, 10)) # 4
    print(bisect.bisect_left(A, 10)) # 4


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