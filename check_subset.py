rloop = int(input())
for i in range(0, rloop):
    sint = int(input())
    aset = set([int(x) for x in input().split()])
    rint = int(input())
    bset = set([int(x) for x in input().split()])
    cset = bset.intersection(aset)
    if aset == cset:
        print(True)
    else:
        print(False)
