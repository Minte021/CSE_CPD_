n, h = map(int, input().split())

height = list(map(int, input().split()))

count = 0
for i in range(n):
    if height[i] > h:
        count += 2
    else:
        count += 1

print(count)