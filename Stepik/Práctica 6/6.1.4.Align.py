from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline
import os
#'''

in_file = 'secuencias_dentista.fasta'
clustal = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Stepik/Práctica 6/clustalw2'

cl = ClustalwCommandline(clustal, infile=in_file)
assert os.path.isfile('/home/naikymen/PycharmProjects/UAB/Bioinformatica/Stepik/Práctica 6/clustalw2'), 'ClustalW2 binary missing'
stdout , stderr = cl()

print(stdout)