n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)
s = sum(a)
b1 = a[0]
m = s / 2
i = 1
c = 1
while not b1 > m:
    c += 1
    if b1 > sum(a[i:]):
        break
    else:
        b1 = b1 + a[i]
    i += 1
print(c)

