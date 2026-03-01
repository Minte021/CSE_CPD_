t = int(input())

for _ in range(t):
    n = int(input())
    m = 0

    while n != 1:
        if n % 6 == 0:
            n //= 6
            m += 1
        elif n % 3 == 0:
            n *= 2
            m += 1
        else:
            m = -1
            break

    print(m)