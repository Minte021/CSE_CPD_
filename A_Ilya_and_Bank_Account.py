n = int(input())
if n >= 0:
    print(n)
else:
    n = str(n)
    l = []
    for i in n:
        l.append(i)
    if l[-1] < l[-2]:
        l.pop(-2)
        p = ""
        for i in l:
            p += str(i)
        print(int(p))
    else:
        l.pop(-1)
        p = ""
        for i in l:
            p += str(i)
        print(int(p))