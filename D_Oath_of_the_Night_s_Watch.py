n = int(input())
x = list(map(int, input().split()))
c = 0
for i in range(0, n-1):
    if x[i+1] - x[i] == 1:
        c += 1

print(c)