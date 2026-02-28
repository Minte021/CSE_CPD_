l = "qwertyuiopasdfghjkl;zxcvbnm,./"
h = input()
s = input()
p = ''
if h == "R":
    for i in s:
        a = l.index(i)
        p += l[a-1]
    print(p)

else:
    for i in s:
        a = l.index(i)
        p += l[a+1]
    print(p)