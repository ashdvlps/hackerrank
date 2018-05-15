#The first line contains the number of elements in set
s = input()
#The second line contains the space separated list of elements in set
sset = set([int(x) for x in input().split()])

#The third line contains integer , the number of other sets.
for i in range(0,int(input())):
    op = input().split()[0]

    other_set = set(set([int(x) for x in input().split()]))

    if op == 'update':
        sset.update(other_set)
    if op == 'intersection_update':
        sset.intersection_update(other_set)
    if op == 'difference_update':
        sset.difference_update(other_set)
    if op == 'symmetric_difference_update':
        sset.symmetric_difference_update(other_set)


print(sum(list(sset)))
