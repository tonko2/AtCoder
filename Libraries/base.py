def base_10_to_n(x, n):
    res = []
    while x:
        res.append(str(x % n))
        x //= n
    res.reverse()
    return "".join(res)

def base_n_to_10(x, n):
    return int(str(x), n)

def main():
    x = 17
    print(base_10_to_n(x, 9))

    str_x = '21'
    print(int(str_x, 8))

    print(base_n_to_10(18, 9))

if __name__ == "__main__":
    main()
