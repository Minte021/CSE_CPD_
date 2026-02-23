n = int(input())
c = 0
for i in range(n):
    x = input()
    if x == "X++" or x == "++X":
        c += 1
    else:
        c -= 1
print(c)