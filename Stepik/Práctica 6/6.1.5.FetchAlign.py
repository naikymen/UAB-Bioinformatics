from Bio import Entrez
from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline

# Archivo donde dejar las secuencias
secuencias = 'secuencias_dentista.fasta'
# Entradas a consultar
entradas = "M90848 M90849 M90850 M90851 M90852 M90853"  # Estas son las del dentista

def consultar(identificador):  # Función para consultar entrez
    Entrez.email = "sample@example.com"
    fetch = Entrez.efetch("nuccore",id=identificador,rettype="gb",retmode="text")
    record = SeqIO.read(fetch,"gb")
    return record


consultas = entradas.split(sep=' ')
consulta = iter(consultas)

out = open(secuencias,'w')
out.close()
out = open(secuencias,'a')

for i in consulta:
    record = consultar(i)
    SeqIO.write(record, out, 'fasta')

out.close()

#''' Un control para saber si se guardó bien

out = open(secuencias,'rU')

for rec in SeqIO.parse(out, 'fasta'):
    print(rec.id)

out.close()

#'''

clustal = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Stepik/Práctica 6/clustalw2'
cl = ClustalwCommandline(clustal, infile=secuencias)
stdout , stderr = cl()

print(stdout)
print(stderr)