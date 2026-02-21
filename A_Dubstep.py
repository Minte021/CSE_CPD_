song = input()
x = song.replace("WUB", " ")
x = x.split()
for i in x:
    print(i, end=" ")