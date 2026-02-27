t = int(input())
for i in range(t):
    n = int(input())
    f = False
    y = n // 2020
    for i in range(y):
        if n - 2020 == 2020 or n - 2020 == 2021:
            f = True
            break
            
        elif (n - 1) - 2021 == 2020 or (n - 1) - 2021 == 2021:
            f = True
            break

        else:
            n = n - 2020
    if f:
        print("YES")
    else:
        print("NO")