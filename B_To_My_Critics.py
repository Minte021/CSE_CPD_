t = int(input())
for i in range(t):
    a = list(map(int, input().split()))
    x = max(a)
    a.remove(x)
    if x + a[0] >= 10 or x + a[1] >= 10:
        print("YES")
    else:
        print("NO")