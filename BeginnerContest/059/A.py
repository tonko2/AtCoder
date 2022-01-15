s1, s2, s3 = map(str, input().split())

s1 = list(map(str, s1))
s2 = list(map(str, s2))
s3 = list(map(str, s3))

print(s1[0].upper() + s2[0].upper() + s3[0].upper())