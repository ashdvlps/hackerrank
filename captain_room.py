from collections import Counter
gsize = int(input())
c = Counter([int(x) for x in input().split()])
for i in c:
    if c[i] != gsize:
        print(i)
