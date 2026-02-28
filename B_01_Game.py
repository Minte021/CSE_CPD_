t = int(input())
for i in range(t):
    s = input()
    z = s.count('0')
    o = s.count('1')
    p = min(z, o)
    if p % 2 == 1:
        print("DA")
    else:
        print("NET")