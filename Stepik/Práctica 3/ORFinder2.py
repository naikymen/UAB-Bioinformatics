from Bio import SeqIO
from Bio.Seq import Seq
import numpy

global file
global record
global sequence
global desde
global hasta
file = '/media/naikymen/SD64/Barcelona UAB/Bioinformática/Stepik 3/sequence2.gb'
record = SeqIO.read(file, 'genbank')
sequence = str(record.seq)
#sequence = iter(sequence)
#seq = Seq('TGA').reverse_complement()
desde = 200
hasta = 500

#start = int()
#end = int()

ORFs = []
state = str('STOP encontrado')
start = int
stop = int


def findstart(d,h):
    for s in range(d,h):
        triplet = str(sequence[s:s + 3])
        if triplet == 'ATG':
            return [s,'START encontrado']
        else:
            s += 2


def findstop(d,h):
    for x in range(d,h):
        triplet = str(sequence[x:x + 3])
        if triplet == 'TAA': #or 'TAG' or 'TGA':
            return [x,'STOP encontrado']
        else:
            x += 2



while state == 'STOP encontrado':
    [start,state] = findstart(desde,hasta)
print('START at: ' + str(start))

while state == 'START encontrado':
    [stop,state] = findstop(start,hasta)
print('STOP at: ' + str(stop))



"""


for s in range(desde,hasta):
    while state == 'STOP encontrado':
        [start,state] = findstart(s,hasta)
    print('STOP at: ' + str(s))
    while state == 'START encontrado':
        [stop,state] = findstop(s,hasta)
    print('START at: ' + str(s))
    ORFs.append([start,stop])

print(ORFs)



    triplet = str(sequence[s:s+3])
    #print(triplet)
    if triplet == 'ATG':
        print(triplet)
        print('START')
        print(s)
        start = s
        while triplet != 'TAA' or 'TAG' or 'TGA':
            for x in range(s,hasta):
                triplet = str(sequence[s:s + 3])
                end = x
                break
        ORF.append([start,end])

print(ORF)




        if triplet == 'CAT':
        stopfw.append(n)
    if triplet == 'TTA' or 'CTA' or 'TCA':
        stoprv.append(n)
"""