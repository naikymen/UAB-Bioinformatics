from Bio import Entrez
from Bio import SeqIO
from textwrap import wrap


def consultar(identificador):  # Función para consultar entrez
    Entrez.email = "sample@example.com"
    fetch = Entrez.efetch("nuccore",id=identificador,rettype="gb",retmode="text")
    record = SeqIO.read(fetch,"gb")
    return record

#entradas = "NM_001159758 NM_001172751 JQ342169 NM_001197168 JX398977 JF927165 NM_001025158 NM_204821 NM_001271262"  # Entradas a comparar, mal??
entradas = "JQ867082 JQ712982 NM_002133 JX317624 NM_001270868 JX308821 JF927163 NM_001079732 JQ342169 JF927165"  # Este anduvo bien
consultas = entradas.split(sep=' ')
consulta = iter(consultas)
record = consultar(next(consulta))  # Consultar la primera
l = record.__len__()
print(l)

# Comparar y consultar las demás entradas
for i in consulta:
    c = consultar(i)
    print(c.__len__())
    if l > c.__len__():
        record = c
        l = c.__len__()

# Dar formato
gi = str(record.annotations["gi"])  # Primary ID
gb = str(record.id)  # Accession dot version
if record.description[-1] == ".":  # Remover el punto final, si  lo hay.
    record.description = record.description[:-1]
secuencia70 = "\n".join(wrap(str(record.seq), 70))  # Secuencia en fasta con 70 caracteres por linea (a lo Perl)

print(">"
      + "|".join(["gi",gi,"gb",gb," "])
      + record.description
      + "\n"
      + secuencia70
      )