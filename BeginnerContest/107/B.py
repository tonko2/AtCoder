H, W = map(int, input().split())
field = [input() for i in range(H)]
cols = list(zip(*field))
for r in field:
    if all([c == '.' for c in r]):
        continue
    line = ''
    for i, c in enumerate(r):
        if all([c == '.' for c in cols[i]]):
            continue
        line += c
    print(line)
