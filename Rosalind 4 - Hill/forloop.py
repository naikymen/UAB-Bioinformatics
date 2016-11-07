#http://stackoverflow.com/questions/1663807/how-can-i-iterate-through-two-lists-in-parallel-in-python

a = iter('CATCGTAATGACGGCCT')
b = iter('GAGCCTACTAACGGGAT')
d = 0

for i,j in zip(a,b):
    if i !=j:
        d += 1

print(d)