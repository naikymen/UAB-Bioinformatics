from Bio import SeqIO
from Bio.Seq import Seq

file = '/media/naikymen/SD64/Barcelona UAB/Bioinformática/Stepik 3/sequence2.gb'
record = SeqIO.read(file, 'genbank')
seq = str(record.seq)
rseq = str(Seq(seq).reverse_complement())

n = 0
s = 0
x = 0

def orfinder(RF, sequence):
    ORFs = []
    hasta = len(sequence)
    #hasta = 615
    state = 'buscar s'
    n = RF
    while n < hasta:
        triplet = str(sequence[n:n + 3])
        if triplet == 'ATG' and state == 'buscar s':
            s = n
            state = 'buscar x'
            #print(triplet)
            #print('START encontrado en: ' + str(s))
        m = int(n)
        while state == 'buscar x' and m <= hasta:
            m += 3
            triplet = str(sequence[m:m + 3])
            if triplet == 'TAA' or triplet == 'TAG' or triplet == 'TGA':
                x = m
                state = 'buscar s'
                if (x-s) >= 63*3:
                    ORFs.append([s, x,x-s])
                    n = int(m)
                break
        n += 3

    return(len(ORFs))


#"""
ftot = 0
print("Forward")
for i in [0,1,2]:
    count = orfinder(i, seq)
    print("Found %s ORFs in RF: %s" % (count, i+1))
    ftot += count
print('Total ORFs in the forward strand: %s'%ftot)

rtot = 0
print("\nReverse")
for i in [0, 1, 2]:
    count = orfinder(i, rseq)
    print("Found %s ORFs in RF: %s" % (count, i+1))
    rtot += count
print('Total ORFs in the reverse strand: %s' % rtot)

#"""
#http://stackoverflow.com/questions/5954260/default-substituting-s-in-python-scripts
#http://stackoverflow.com/questions/4693120/use-of-global-keyword-in-python
# 159 en el RF1
# 436/9 forward
# 358/64 reverse