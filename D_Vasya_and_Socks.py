n, m = map(int, input().split())
s = n
d = 0
while s > 0:
    d += 1
    s -= 1
    if d % m == 0:
        s += 1
print(d)
