n = int(input())
gravity = list(map(int, input().split()))

gravity.sort()

for i in gravity:
    print(i, end=" ")