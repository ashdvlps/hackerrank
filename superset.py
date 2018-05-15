aset = set([int(x) for x in input().split()])
res = False
for i in range(0, int(input())):
    oset = set([int(x) for x in input().split()])
    if len(aset) <= len(oset):
        res = False
        break
    else:
        if oset == aset.intersection(oset):
            res = True
        else:
            res = False
            break
print(res)
