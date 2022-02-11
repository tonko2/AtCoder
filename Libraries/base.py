def base_10_to_n(x, n):
    res = []
    while x:
        res.append(str(x % n))
        x //= n
    res.reverse()
    return "".join(res)

def main():
    x = 17
    print(base_10_to_n(x, 9))

    str_x = '21'
    print(int(str_x, 8))

if __name__ == "__main__":
    main()
