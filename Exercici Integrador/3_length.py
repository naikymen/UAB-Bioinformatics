from Bio import SeqIO

file = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Exercici Integrador/grup_3.fasta'
record = SeqIO.read(file,'fasta')  # se usa read si tiene uno, parse si tiene varios

length = len(record.seq)