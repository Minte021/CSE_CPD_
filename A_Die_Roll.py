x , y = list(map(int, input().split()))
    
m = max(x,y)
e = 7 - m
if e % 2 == 0:
    if e == 6:
        print(f"{1}/{1}")
    else:
        d = e // 2
        print(f"{d}/{6//2}")
elif e % 3 == 0:
    d = e // 3
    print(f"{d}/{6//3}")
else:
    print(f"{e}/{6}")