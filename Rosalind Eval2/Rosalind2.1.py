# compute GC content
from Bio import SeqIO
from Bio import SeqUtils
import operator

file = open('intest2.fasta','r')
output = open('outest2.fasta','w')
#https://docs.python.org/2/library/functions.html
records = SeqIO.parse(file, 'fasta')
gc = {}


window = 10
step = 10


if window != step:
    print('Warning, step is not equal to window size.\nResults will not be exact.\n')

for record in records:
    count = 0
    i = 0
    k = 0
    id = record.id
    seq = record.seq

    while i < (len(seq)-window):
        finestra = seq[i:i+window]
        count += (finestra.count('G') + finestra.count('C'))
        i += step
        k += len(finestra)

    finestra = seq[i:]
    k += len(finestra)
    count += (finestra.count('G') + finestra.count('C'))
    gc[id] = 100*count/k

# Buscar y devolver el valor máximo
maxid = max(gc.items(), key=operator.itemgetter(1))[0]
print(maxid)
print(round(gc[maxid],6))


file.close()
output.close()