t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    c = 1
    d = 1
    if x % 2 == 0 and y % 2 == 0:
        while x % 2 == 0 and x != 0:
            x /= 2
            c  *= 2
        while y % 2 == 0 and x != 0:
            y /= 2
            d *= 2
    elif x % 2 == 0:
        while x % 2 == 0 and x != 0:
            x /= 2
            c  *= 2
    elif y % 2 == 0:
        while y % 2 == 0:
            y /= 2
            d *= 2
    
    if c*d >= z:
        print("YES")
    else:
        print("NO")