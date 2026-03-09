num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
num1.extend(num2)
num1.sort()
l = len(num1)
if l % 2 == 0:
    m = num1[l//2 - 1] + num1[l//2]
    print(m/2)
else:
    m = num1[l // 2]
    print(m)