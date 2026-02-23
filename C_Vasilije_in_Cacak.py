t = int(input())
for i in range(t):
    n, k, x = map(int, input().split())
    a1 = n - k + 1
    min_bd = k * (k + 1) / 2
    max_bd = k * ((2 * a1) + k - 1) / 2
    if min_bd <= x <= max_bd:
        print("YES")
    else:
        print("NO")
