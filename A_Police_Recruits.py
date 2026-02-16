n = int(input())
l = list(map(int, input().split()))

p = 0
c = 0

for i in l:
    if i == -1:
        if p > 0:
            p -= 1
        else:
            c += 1
    else:
        p += i
        
print(c)
