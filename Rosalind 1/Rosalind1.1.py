from Bio import Entrez
from Bio import SeqIO
from Bio import SeqUtils
from Bio import Seq
import Bio.GenBank
from textwrap import wrap

# https://www.ncbi.nlm.nih.gov/genbank/sequenceids/
# https://www.biostars.org/p/66921/


def consultar(identificador):
    fetch = Entrez.efetch("nuccore",id=identificador,rettype="gb",retmode="text")
    record = SeqIO.read(fetch,"gb")
    return record

Entrez.email = "sample@example.com"
#resultado = Bio.SeqRecord.SeqRecord
consultas = "FJ817486 JX069768 JX469983".split(sep=' ')
#consultas = [57240072, 57240071]

consulta = iter(consultas)
record = consultar(next(consulta))
l = record.__len__()

for i in consulta:
    c = consultar(i)
    if l > c.__len__():
        record = c
        l = c.__len__()

#print(record.description)

gi = str(record.annotations["gi"])  # Primary ID
gb = str(record.id)  # Accession dot version
if record.description[-1] == ".":  # Volar el punto final, si  lo hay.
    record.description = record.description[:-1]
#secuencia = (record.format("fasta").split("\n"))
#secuencia = "\n".join(secuencia[1:])
secuencia70 = "\n".join(wrap(str(record.seq), 70))

print(">"
      + "|".join(["gi",gi,"gb",gb," "])
      + record.description
      + "\n"
      + secuencia70
      )



"""

for i in consultas:
    record = consultar(i);
    l = record.__len__();




gi = str(resultado.annotations["gi"])  # Primary ID
gb = str(resultado.id)  # Quizas sea gb id?)
#output["accessions"] = resultado.annotations["accessions"]
#output["version"] = (resultado.annotations["sequence_version"])

print(
    "|".join(["gi",gi,"gb",gb]) + "|" + resultado.seq
)


print(record.format("gb"))

print(record.format("fasta"))

"""