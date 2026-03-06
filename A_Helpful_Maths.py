s = input()
num = []
opr = []
for i in s:
    if i == '+':
        opr.append(i)
    else:
        num.append(i)
num.sort()
k = 1
for i in opr:
    num.insert(k, i)
    k += 2
for i in num:
    print(i, end="")