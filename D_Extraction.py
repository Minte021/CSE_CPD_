tn = int(input())
n = []
for i in range(tn):
    t = input()
    t = list(t)
    p = 0
    k = len(t) - 1
    n.clear()
    for i in t:
        p = int(i) * (10 ** k)
        if p > 0:
            n.append(p)
        k -= 1
    print(len(n))
    for i in n:
        print(i, end=" ")
    print()

