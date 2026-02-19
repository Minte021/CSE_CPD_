t = int(input())
r = []
def min_move(x,y):
    c = 0
    while x % y != 0:
        x += 1
        c += 1
    print(c)

for i in range(t):
    a, b = map(int, input().split())
    min_move(a,b)