y = int(input())

f = y + 1

while f > y:
    f = str(f)
    if len(set(f)) == len(f):
        print(f)
        break
    f = int(f)
    f += 1