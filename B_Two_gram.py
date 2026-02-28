from collections import Counter
n = int(input())
s = input()
l = []
for i in range(len(s) - 1):
    l.append(s[i]+s[i+1])
f = Counter(l)
print(max(f, key=f.get))