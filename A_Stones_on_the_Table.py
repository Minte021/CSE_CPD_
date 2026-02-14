n = int(input())
c = input()
count = 0

for i in range(0, len(c) - 1):
    if c[i] == c[i + 1]:
        count += 1


print(count)
