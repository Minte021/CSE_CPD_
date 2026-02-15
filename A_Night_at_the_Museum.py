alphabets = "abcdefghijklmnopqrstuvwxyz"
w = input()

w_index = []
w_index.append(0)
for i in w:
    x = alphabets.index(i)
    if x > 13:
        m = 26 - x
        w_index.append(m)
    else:
        w_index.append(x)
w_index.sort()
q = []
for i in range(len(w_index) - 1):
    p = w_index[i] + w_index[i + 1]
    if p <= 13:
        q.append(p)
    else:

        p = abs(w_index[i + 1] - w_index[i])
        q.append(p)
print(sum(q))