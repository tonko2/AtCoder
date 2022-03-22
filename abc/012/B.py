N = int(input())

hh = N // 3600
mm = (N - hh * 3600) // 60
ss = N % 60

print('%02d:%02d:%02d' % (hh, mm, ss))
