from Bio import SeqUtils

def traducir(secuencia):
    fw_rv = [secuencia.reverse_complement(), secuencia]
    strand = -1
    for seq in fw_rv:
        for frame in [2,1,0]:
            print(
                seq[frame:len(seq)-3+frame].translate(), ' (', strand*(frame+1), ')',
            sep='')
        strand = -strand