t = int(input())
for i in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        l, r, k = map(int, input().split())
        temp = a.copy()
        for i in range(l-1, r):
            temp[i] = k
        if sum(temp) % 2 != 0:
            print("YES")
        else:
            print("NO")
        del temp