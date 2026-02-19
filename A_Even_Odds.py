n, k = map(int, input().split())
odd = []
even = []
for i in range(1, n + 1, 2):
    odd.append(i)
for j in range(2, n + 1, 2):
    even.append(j)

odd.extend(even)
odd.sort()
print(odd)