a = "abcabcbb"
a = list(a)
l1 = []
l2 = []

for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] != a[j]:
            l1.append(a[i])
            l1.append(a[j])
        else:
            l2.extend([l1])
            l1.clear()
            break
print(l2)

    





