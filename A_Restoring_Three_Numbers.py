x = list(map(int, input().split()))
x.reverse()
r = []
for i in x:
    a = max(x)
    if a == i:
        continue
    else:
        r.append(a - i)

for j in r:
    print(j, end=" ")