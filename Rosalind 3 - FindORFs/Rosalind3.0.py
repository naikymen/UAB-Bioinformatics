#Open Reading Frames
from Bio import SeqIO
from Bio import SeqUtils
import Bio

test_seq = open('test.txt')
records = SeqIO.parse(test_seq,'fasta')
starts = ['ATG']
stops = ['TAA','TAG','TGA']
results = []


def inframe(pos, sec, l):
    stop = len(sec) - (len(sec)%3)
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
    fw_rv = [rec.seq.reverse_complement(),rec.seq]
    largo = len(rec.seq)
    strand = -1
    for seq in fw_rv:
        for rf in [1,2,3]:
            n = rf -1
            while n <= largo-3:
                [s, x, n] = inframe(n,seq,largo)
                if s != -1:
                    trans = seq[s:x].translate()
                    results.append([trans.tostring(), strand*rf])
        strand = -strand

for record in records:
    secuencia = SeqUtils.six_frame_translations(record.seq)
    print(secuencia)
    findorf(record)

for k in results:
    print(k[0])