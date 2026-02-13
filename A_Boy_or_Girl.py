x = input()
char = []
count  = 0
for i in x:
    if i not in char:
        char.append(i)
    else:
        continue
for i in char:
    count += 1
if not count % 2 == 0:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")