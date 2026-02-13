s = input()

capital = 0
small = 0
for i in s:
    if i != i.lower():
        capital += 1
    else:
        small += 1
if small >= capital:
    print(s.lower())
else:
    print(s.upper())