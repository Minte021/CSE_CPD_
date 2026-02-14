n = int(input())
fb = []
for i in range(n):
    fb.append(list(map(int, input().split())))
count = 0
for i in fb:
    for j in fb:
        if i != j and i[0] == j[1]:
            count += 1
print(count)