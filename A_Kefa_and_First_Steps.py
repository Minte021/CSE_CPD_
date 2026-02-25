n = int(input())
a = list(map(int, input().split()))
a.append(-1)
t = []
c = 1
for i in range(0, len(a) - 1):
    if a[i] <= a[i+1]:
        c += 1
    else:
        t.append(c)
        c = 1
print(max(t))