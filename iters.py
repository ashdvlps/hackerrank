from itertools import combinations
inp = input()
a = [x for x in input().split()]
ci = int(input())
c = combinations(a, ci)
s = list(c)
d = 0

for row in s:
    if 'a' in row:
        d += 1

print(round(d/len(s),4))
