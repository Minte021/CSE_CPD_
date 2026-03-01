#CSEC_CPD_Lab2_F
from collections import Counter
n = int(input())
a = list(map(int, input().split()))
x = Counter(a)
print(len(a) - max(x.values()))