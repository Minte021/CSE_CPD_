n, m = map(int, input().split())
c = 1
while n != 1 or m != 1:
    if m == 1 or n == 1:
        break
    n -= 1
    m -= 1
    c += 1

if c % 2 == 0:
    print("Malvika")
else:
    print("Akshat")