a = list(map(int, input().split()))
n = input()

rept = dict.fromkeys(['1', '2', '3', '4'], 0)

for i in n:
    if i in rept:
        rept[i] += 1
o = []   
for j in rept.values():
    o.append(j)
cal = []
for i,j in zip(a, o):
    p = i * j
    cal.append(p)

print(sum(cal))