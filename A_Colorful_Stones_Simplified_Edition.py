s = input()
t = input()
c = 0
count = 1
for i in t:
    if i == s[c]:
        count += 1 
        c += 1
            
print(count)