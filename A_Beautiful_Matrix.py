mat = []
for i in range(5):
    mat.append(list(map(int, input().split())))
row1 = 0
for i in mat:
    if sum(i) == 1:
        break
    row1 += 1

col1 = 0
for j in mat[row1]:
    if j == 1:
        break
    col1 += 1

row = row1 + 1
column = col1 + 1

mat_mid = abs(row - 3) + abs(column - 3)

print(mat_mid)
