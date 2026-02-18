n = int(input())
b = list(map(int, input().split()))
m = int(input())

for i in range(m):
    a,c = list(map(int, input().split()))
    a-=1
    if a==0:
        r=b.pop(a)
        b.insert(a,0)
        b[a+1]+=r-c
        
    elif a==n-1:
        b[a-1]+=c-1
        b[a]=0
    else:
        r=b.pop(a)
        b.insert(a,0)
        b[a-1]+=c-1
        b[a+1]+=r-c
for i in b:
    print(i)

    
