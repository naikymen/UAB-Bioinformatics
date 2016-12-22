from Bio import SeqIO
from Bio.Blast import NCBIWWW

file = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Exercici Integrador/grup_3.fasta'
record = SeqIO.read(file,'fasta')  # se usa read si tiene uno, parse si tiene varios

result_handle = NCBIWWW.qblast("blastn", "nt",  record.format('fasta'))

save_file = open("/home/naikymen/PycharmProjects/UAB/Bioinformatica/Exercici Integrador/my_blast.xml", "w")
save_file.write(result_handle.read())
save_file.close()

result_handle.close()