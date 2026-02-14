x, y = map(int, (input().split()))
i = 1
c = 0
while True:
    p = (x * i) - y
    if p % 10 == 0 or (x * i) % 10 == 0:
        break
    i += 1
print(i)