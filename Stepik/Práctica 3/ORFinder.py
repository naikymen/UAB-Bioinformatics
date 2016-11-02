from Bio import SeqIO
from Bio.Seq import Seq
import numpy

file = '/media/naikymen/SD64/Barcelona UAB/Bioinformática/Stepik 3/sequence2.gb'
record = SeqIO.read(file, 'genbank')
sequence = str(record.seq)
length = len(sequence)

startfw = []
startrv = []
stopfw = []
stoprv = []


n=0

#seq = Seq('TGA').reverse_complement()

for n in range(0,10000):
    triplet = str(sequence[n:n+3])
    if triplet == 'ATG':
        startfw.append(n)
    if triplet == 'CAT':
        startrv.append(n)
    if triplet == 'TAA' or 'TAG' or 'TGA':
        stopfw.append(n)
    if triplet == 'TTA' or 'CTA' or 'TCA':
        stoprv.append(n)

rvl = (len(startfw))
fwl = (len(stopfw))
#fwmatrix = matrix((len(startfw),len(stopfw)))
dummy = numpy.matrix([[1, 2], [3, 4]])
print(dummy)
print(dummy[:,1]) # Columna

mat = (numpy.zeros((fwl,rvl)))

for n in fwl:
    mat[n]
