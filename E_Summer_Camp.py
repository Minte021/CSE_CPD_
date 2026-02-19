n = int(input())
l = []
for i in range(1, n + 1):
    l.append(str(i))
a = ''
for i in l:
    a += i
print(a[n - 1])