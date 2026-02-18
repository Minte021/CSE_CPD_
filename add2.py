l1 = [0]
l2 = [0]
l1.reverse()
l2.reverse()
x = ''
y = ''
for i in range(0, len(l1)):
    x += str(l1[0])
    y += str(l2[0])
    l1.remove(l1[0])
    l2.remove(l2[0])

x = int(x)
y = int(y)

s = x + y
s = str(s)

r = []
for i in s:
    r.append(i)

n = r.reverse()
print(r)
