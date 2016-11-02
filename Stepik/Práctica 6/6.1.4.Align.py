from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline
import os
from Bio import AlignIO
#'''

in_file = 'secuencias2.fasta'
out_file = 'secuencias2.aln.fasta'
clustal = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Stepik/Práctica 6/clustalw2'

cl = ClustalwCommandline(clustal, infile=in_file)
assert os.path.isfile('/home/naikymen/PycharmProjects/UAB/Bioinformatica/Stepik/Práctica 6/clustalw2'), 'ClustalW2 binary missing'
stdout , stderr = cl()

#print(stdout)

allignment = open('secuencias2.aln', 'r+')
a_handle = AlignIO.read(allignment, 'clustal')
allignment.close()

#print(a_handle)
AlignIO.write(a_handle,out_file,'fasta')