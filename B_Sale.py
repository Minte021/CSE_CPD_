n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
s = 0
for i in range(0, m):
    if a[i] <= 0:
        s += a[i]
print(abs(s))