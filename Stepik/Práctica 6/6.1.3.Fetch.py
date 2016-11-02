from Bio import Entrez
from Bio import SeqIO
from textwrap import wrap
#'''

secuencias = 'secuencias.fasta'
out = open(secuencias,'w')
out.close()

def consultar(identificador):  # Función para consultar entrez
    Entrez.email = "sample@example.com"
    fetch = Entrez.efetch("nuccore",id=identificador,rettype="gb",retmode="text")
    record = SeqIO.read(fetch,"gb")
    return record

entradas = "M90848 M90849 M90850 M90851 M90852 M90853 M90855 M90863 M90880 M90882 M90888 M90894 M90901 M90917 M90929 M90939 M90956 M90957 M90964"
consultas = entradas.split(sep=' ')
consulta = iter(consultas)

out = open(secuencias,'a')

for i in consulta:
    record = consultar(i)
    SeqIO.write(record, out, 'fasta')  # Si las guardo en gb, no logro que el clustalw2 las tome

out.close()

#'''

handle = open(secuencias,'rU')

for rec in SeqIO.parse(handle, 'fasta'):
    print(rec.id)

handle.close()

#'''
