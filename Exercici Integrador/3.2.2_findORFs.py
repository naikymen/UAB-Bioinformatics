#Open Reading Frames
#Incluir nested ORFs

from Bio import SeqIO
from Bio import SeqUtils
import Bio

test_seq = open('/home/naikymen/PycharmProjects/UAB/Bioinformatica/Exercici Integrador/grup_3.fasta','r')
test_out = open('3.2.2_foundORFs.txt','w')
test_out.close()
test_out = open('3.2.2_foundORFs.txt','a')
record = SeqIO.read(test_seq,'fasta')
starts = ['ATT', 'ATC', 'ATA', 'ATG', 'GTG']  # Con la onda mitocondrial...
stops = ['TAA', 'TAG', 'AGA', 'AGG'] # sacada de acá http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc25
loco = SeqUtils.Seq('ATG').translate()


def inframe(pos, sec, l):
    stop = -1
    start = -1
    while pos < (l - 2):
        trip = (sec[pos:pos + 3])
        if trip in starts:
            start = pos
            break
        pos += 3

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
                    protein = str(seq[s:x].translate(table="Vertebrate Mitochondrial"))
                    results.append([protein, strand*rf, s, x])
                    n = s + 3
        strand = -strand
    return results

output = findorf(record)

final = set()
for k in output:
    final.add(k[0])

for j in final:
    test_out.write(j)
    test_out.write('\n')

for j in output:
    print(j)

test_out.close()
test_seq.close()