n, m = map(int, input().split())
f = list(map(int, input().split()))
f.sort()
i = 0
r = []
while n != m + 1:
    x = f[i:n]
    a = max(x) - min(x)
    r.append(a)
    i += 1
    n += 1
print(min(r))