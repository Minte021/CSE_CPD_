n = int(input())
a = list(map(int, input().split()))
m = int(input())

for i in range(m):
    x,y = list(map(int, input().split()))

    x -= 1
    l = y - 1
    r = a[x] - y

    if x - 1 >= 0:
        a[x - 1] += l

    if x + 1 < n:
        a[x + 1] += r

    a[x] = 0

for i in a:
    print(i)