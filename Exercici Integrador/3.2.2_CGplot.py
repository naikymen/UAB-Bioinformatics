# compute GC content
# Code adapted from 'Rosalind 2.1'
from Bio import SeqIO
import pylab

file = open('/home/naikymen/PycharmProjects/UAB/Bioinformatica/Exercici Integrador/grup_3.fasta','r')
records = SeqIO.parse(file, 'fasta')

gc = {}
gc_plot = [[]]
window = 20
step = 5
j = 0

for record in records:
    count = 0
    i = 0
    k = 0
    id = record.id
    seq = record.seq

    while i < (len(seq)-window):
        finestra = seq[i:i+window]
        count += (finestra.count('G') + finestra.count('C'))
        gc_plot[j].append(finestra.count('G') + finestra.count('C'))
        i += step
        k += len(finestra)

    finestra = seq[i:]
    k += len(finestra)
    count += (finestra.count('G') + finestra.count('C'))
    gc[id] = 100*count/k
    j += 1

print(gc_plot)


file.close()