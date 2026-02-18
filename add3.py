l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
if len(l1) != len(l2):
    if len(l1) < len(l2):
        d = len(l2) - len(l1)
        for i in range(d):
            l1.append(0)
    else:
        d = len(l1) - len(l2)
        for i in range(d):
            l2.append(0)
l1.reverse()
l2.reverse()

x = ''
y = ''

for i in range(len(l1)):
    x += str(l1[0])
    y += str(l2[0])
    l1.remove(l1[0])
    l2.remove(l2[0])

x = int(x)
y = int(y)

s = x + y
s = str(s)

f = []
for i in s:
    f.append(i)
return f.reverse()