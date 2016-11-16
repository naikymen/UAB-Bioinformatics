file = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Rosalind 9 - N50_N75/input3.txt'
handle = open(file,'r')
records = handle.readlines()

lengths = []
a = []
b = []
total = 0
l = 0
k = 0
n50 = 0
n75 = 0
n100 = 0

for record in records:
    length = len(record.rstrip('\n'))
    total += length
    lengths.append(length)
lengths.sort()

for i in range(len(lengths)):
    l += lengths[i]
    if l >= total*(50/100) and n50 == 0:
        if lengths[i] != lengths[i-1]:
            n50 = lengths[i]
    if l >= total*(75/100) and n75 == 0:
        if lengths[i] != lengths[i-1]:
            n75 = lengths[i]
    if l >= total*(100/100) and n100 == 0:
        if lengths[i] != lengths[i-1]:
            n100 = lengths[i]
    i += 1

print(n50, n75)










'''
sortedLengths = iter(sorted(lengths))
# https://wiki.python.org/moin/HowTo/Sorting

while l <= total*(50/100):
    k = next(sortedLengths)
    l += k
    print(l, k, l / total)
n50 = k
print('n50 --',k)

while l <= total*(75/100):
    k = next(sortedLengths)
    l += k
    print(l, k, l / total)
n75 = k
print('n75 --',k)

while l <= total*(100/100)-k:
    k = next(sortedLengths)
    l += k
    print(l,k,l/total)
n100 = k
print('n100 --',k)

print('\n')
print(n50, n75)

#'''