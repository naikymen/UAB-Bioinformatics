from Bio import Entrez
from Bio import SeqIO
from textwrap import wrap
#'''

out = open('secuencias_dentista.fasta','w')
out.close()

def consultar(identificador):  # Función para consultar entrez
    Entrez.email = "sample@example.com"
    fetch = Entrez.efetch("nuccore",id=identificador,rettype="gb",retmode="text")
    record = SeqIO.read(fetch,"gb")
    return record

entradas = "M90848 M90849 M90850 M90851 M90852 M90853"  # Solo las del dentista
consultas = entradas.split(sep=' ')
consulta = iter(consultas)

out = open('secuencias_dentista.fasta','a')

for i in consulta:
    record = consultar(i)
    SeqIO.write(record, out, 'fasta')  # Si las guardo en gb, no logro que el clustalw2 las tome

out.close()

#'''

handle = open('secuencias_dentista.fasta','rU')

for rec in SeqIO.parse(handle, 'fasta'):
    print(rec.id)

handle.close()

#'''
