# compute GC content
from Bio import SeqIO
from Bio import SeqUtils

file = open('/media/naikymen/SD64/Barcelona UAB/Bioinformática/Rosalind Eval2/secuencia.fasta','r')
output = open('/media/naikymen/SD64/Barcelona UAB/Bioinformática/Rosalind Eval2/output2.fasta','a')
#https://docs.python.org/2/library/functions.html

records = SeqIO.parse(file, 'fasta')
window = 10
step = 10
i = 0
j = 0
gc = {}
GC = {}
gcfreq = []

#"""
for record in records:
    id = record.id
    seq = record.seq
    tcount = seq.count('G') + seq.count('C')
    print('Contenido total: %s' % str(100*tcount/len(seq)))
    print(SeqUtils.GC(seq))
    output.write('>' + id + '\n')

    while i < (len(seq)-window):
        finestra = seq[i:i+window]
        print(finestra)
        count = (finestra.count('G') + finestra.count('C'))
        print(100*count/len(finestra))
        #print(SeqUtils.GC(finestra))
        gcfreq.append(100 * count / len(finestra))
        #output.write()
        j += 1
        i += step

    gc[id] = sum(gcfreq)/j
    GC[id] = SeqUtils.GC(seq)

    #print(sum(gcfreq)/j)

    i = 0
    j = 0
    gcfreq.clear()

#print(GC.values())
#print(gc.values())


file.close()
output.close()

"""
for record in records:
    id = record.id
    seq = record.seq
    tcount = seq.count('G') + seq.count('C')
    print('Contenido total: %s' % str(100*tcount/len(seq)))

    for i in range(0,len(seq)-window):
        finestra = seq[i:i+window]
        print(finestra)
        fcount = finestra.count('G') + finestra.count('C')
        print(100*fcount/window)


record = next(records)
seq = record.seq
print(
    seq[1:10]
)



for a in gc.items():
    print(a)

for a in GC.items():
    print(a)
"""