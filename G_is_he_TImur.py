t = int(input())
m = list("Timur")
m.sort()
for i in range(t):
    n = int(input())
    s = input()
    s = list(s)
    s.sort()
    if s == m:
        print("YES")
    else:
        print("NO")
