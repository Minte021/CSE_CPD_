n, k = map(int, input().split())
if k <= (n + 1) // 2:
    an = (2 * k) - 1
    print(an)
else:
    k -= (n + 1) // 2
    an = 2 * k
    print(an)