#Open Reading Frames
#Incluir nested ORFs

from Bio import SeqIO
from Bio import SeqUtils
import Bio

test_seq = open('test.txt')
records = SeqIO.parse(test_seq,'fasta')
starts = ['ATG']
stops = ['TAA','TAG','TGA']


def inframe(pos, sec, l):
    stop = -1
    start = -1
    while pos < (l - 2):
        print('buscando start',sec[:pos+3])
        trip = (sec[pos:pos + 3])
        if trip in starts:
            start = pos
            print(pos,'S!')
            break
        pos += 3

    #if start == -1:
    #    return [start, stop, pos]

    while pos < (l - 2):
        print('buscando STOP',sec[:pos+3],pos,pos+3)
        trip = (sec[pos:pos + 3])
        if trip in stops:
            print(pos,'Stop!')
            stop = pos
            break
        pos += 3
    print([start, stop, pos])
    return[start, stop, pos]


def findorf(rec):
    fw_rv = [rec.seq.reverse_complement(), rec.seq]
    largo = len(rec.seq)
    strand = -1
    results = []
    for seq in fw_rv:
        for n in [0, 1, 2]:
            rf = n + 1
            while n <= largo-3:
                [s, x, n] = inframe(n,seq,largo)
                if s != -1 and x !=-1:
                    protein = str(seq[s:x].translate())
                    results.append([protein, strand*rf, n])
                    #print(SeqUtils.Seq('ATGCTACTCGGATCATTCAGGCTTATTCCAAAAGAGACTCTAATCCAAGTCGCGGGGTCATCCCCATGTAACCTGA').translate())
        strand = -strand
    return results

for record in records:
    output = findorf(record)


print('\n')

for k in output:
    print(k)
