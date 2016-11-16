file = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Rosalind 9 - N50_N75/input.txt'

records = open(file,'r').readlines()

i = []
total = 0
l = 0
k = 0

for record in records:
    length = len(record.rstrip('\n'))
    total += length
    i.append(length)

j = iter(sorted(i))

while l <= total*(50/100)-k:
    k = next(j)
    l += k

n50 = k

while l <= total*(75/100)-k:
    k = next(j)
    l += k

n75 = k

print(n50,n75)