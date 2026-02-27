t = int(input())
k = "codeforces"
for i in range(t):
    s = input()
    c = 0
    for i, j in zip(k, s):
        if i == j:
            continue
        else:
            c += 1
    print(c)