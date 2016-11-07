#Open Reading Frames
#Incluir nested ORFs

from Bio import SeqIO
from Bio import SeqUtils
import Bio

test_seq = open('test1.in','r')
test_out = open('test1.out','w')
test_out.close()
test_out = open('test1.out','a')
record = SeqIO.read(test_seq,'fasta')
starts = ['ATG']
stops = ['TAA','TAG','TGA']
loco = SeqUtils.Seq('ATG').translate()


def traducir(secuencia):
    fw_rv = [secuencia.reverse_complement(), secuencia]
    strand = -1
    for seq in fw_rv:
        for frame in [2,1,0]:
            print(
                seq[frame:len(seq)-3+frame].translate(), ' (', strand*(frame+1), ')',
                sep='')
        strand = -strand


def inframe(pos, sec, l):
    stop = -1
    start = -1
    while pos < (l - 2):
        trip = (sec[pos:pos + 3])
        if trip in starts:
            start = pos
            break
        pos += 3

    #if start == -1:
    #    return [start, stop, pos]

    while pos < (l - 2):
        trip = (sec[pos:pos + 3])
        if trip in stops:
            stop = pos
            break
        pos += 3
    return[start, stop, pos]


def findorf(rec):
    fw_rv = [rec.seq.reverse_complement(), rec.seq]
    largo = len(rec.seq)
    strand = -1
    results = []
    for seq in fw_rv:
        for n in [2, 1, 0]:
            rf = n + 1
            while n <= largo-3:
                [s, x, n] = inframe(n,seq,largo)
                if s != -1 and x !=-1:
                    protein = str(seq[s:x].translate())
                    results.append([protein, strand*rf, s, x])
                    n = s + 3
                    #print(SeqUtils.Seq('ATGCTACTCGGATCATTCAGGCTTATTCCAAAAGAGACTCTAATCCAAGTCGCGGGGTCATCCCCATGTAACCTGA').translate())
        strand = -strand
    return results


traducir(record.seq)
output = findorf(record)

print('\n')

for k in output:
    print(k)

final = set()
for k in output:
    final.add(k[0])

print(final)

for j in final:
    print(j)
    test_out.write(j)
    test_out.write('\n')

test_out.close()
test_seq.close()