h,m = map(int, input().split())

if m >= 45:
    m = m - 45
else :
    m = m +60 -45
    h = h -1
    if h < 0:
        h = 23
print(h,m)