yyyy, mm, dd = map(int, input().split("/"))

if 2019 >= yyyy:
    if 4 >= mm:
        if 30 >= dd:
            print("Heisei")
        else:
            print("TBD")
    else:
        print("TBD")
else:
    print("TBD")
