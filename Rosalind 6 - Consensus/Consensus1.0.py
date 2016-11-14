from Bio import SeqIO

file = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Rosalind 6 - Consensus/input.fa'
handle = SeqIO.parse(file,'fasta')

def bXn(base):
    if base == 'A': return 0
    if base == 'C': return 1
    if base == 'G': return 2
    if base == 'T': return 3
    if base == 0: return 'A'
    if base == 1: return 'C'
    if base == 2: return 'G'
    if base == 3: return 'T'

records = iter(handle)
record = next(records)
w,h = len(record.seq),4
r = [[0 for x in range(w)] for y in range(h)]

for x in range(w):
    n = bXn(record.seq[x])
    r[n][x] += 1

for record in records:
    for x in range(w):
        n = bXn(record.seq[x])
        r[n][x] += 1

s = [[j[i] for j in r] for i in range(w)]

k = 0
for i in r:
    print(bXn(k) + ': ' + ' '.join(str(x) for x in i))
    k += 1


for i in s:
    print(' '.join(str(x) for x in i))

print(s)
c = ''
for position in s:
    index_min = max(range(len(position)), key=position.__getitem__)
    c += bXn(index_min)

print(c)