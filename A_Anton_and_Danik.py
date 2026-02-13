n = int(input())
pt = []
s = input()
for i in s:
    pt.append(i)

countA = 0
countD = 0
for i in pt:
    if i == 'A':
        countA += 1
    else:
        countD += 1
if countA > countD:
    print("Anton")
elif countA < countD:
    print("Danik")
else:
    print("Friendship")