alphabets = "abcdefghijklmnopqrstuvwxyz"
w = input()
w = "a" + w

l = []

for i in range(0, len(w) - 1):
    x = alphabets.index(w[i])
    y = alphabets.index(w[i+1])
    d = abs(x - y)
    min_d = min(d, 26 - d)
    l.append(min_d)
print(sum(l))
