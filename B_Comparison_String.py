t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    c = 1
    m = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            c += 1
            m = max(m, c)
        else:
            c = 1
    print(m + 1)