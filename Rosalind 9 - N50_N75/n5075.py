file = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Rosalind 9 - N50_N75/input3.txt'
handle = open(file,'r')
records = handle.readlines()

lengths = []
a = []
b = []
total = 0
l = 0
k = 0

for record in records:
    length = len(record.rstrip('\n'))
    total += length
    lengths.append(length)

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
print(n50,n75)