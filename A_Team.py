n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
x = 0
for i in a:
    s = sum(i)
    if s >= 2:
        x += 1

print(x)