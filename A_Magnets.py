n = int(input())
magnet = []
for i in range(n):
    magnet.append(list(map(str, input().split())))

new_magnet = []
x = magnet[0]
new_magnet.append(x)
j = 0

for i in magnet:
    if i != new_magnet[j]:
        new_magnet.append(i)
        j += 1

print(len(new_magnet))