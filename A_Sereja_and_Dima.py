n = int(input())
cards = list(map(int, input().split()))

c = []
s = []
d = []

for i in range(len(cards)):
    if cards[0] > cards[-1]:
        x = cards[0]
        c.append(x)
        cards.remove(x)
    else:
        x = cards[-1]
        c.append(x)
        cards.remove(x)
for i in range(len(c)):
    if i % 2 == 0:
        s.append(c[i])
    else:
        d.append(c[i])


print(sum(s), sum(d))