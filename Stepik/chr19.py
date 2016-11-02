#ch = open('/media/naikymen/SD64/Barcelona 2016/UAB/Bioinformática/Stepik 1.3/ch19.fasta','r')
#lines = ch.readlines()
from Bio import SeqIO
from Bio import SeqUtils
seq_record = SeqIO.read("/media/naikymen/SD64/Barcelona 2016/UAB/Bioinformática/Stepik 1.3/ch19.fasta",'fasta')

#gcskew = SeqUtils.GC_skew() #NO ANDA
#print(gcskew)

#gc = SeqUtils.GC(seq_record.seq)
#print(gc)

"""
A	15142293		0.2583232	0.2500000	1.0332930
C	13954580		0.2380612	0.2500000	0.9522448
G	14061132		0.2398789	0.2500000	0.9595158
T	15282753		0.2607195	0.2500000	1.0428778
"""

gcskew = (14061132-13954580)/(13954580+14061132)
print(gcskew)

atskew = (15142293-15282753)/(15282753+15142293)
print(atskew)