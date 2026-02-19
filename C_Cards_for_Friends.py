t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    if z == 1:
        print("YES")
    elif x == y and (x % 2 != 0 and y % 2 != 0):
        print("NO")
    else:
        cut = x * y
        if cut >= z:
            print("YES")
        else:
            print("NO")