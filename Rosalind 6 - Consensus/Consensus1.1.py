from Bio import SeqIO

file = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Rosalind 6 - Consensus/input.fa'
handle = SeqIO.parse(file,'fasta')

def bXn(o):  # Función útil para pasar de base a índice al manipular las listas
    if o == 'A': return 0
    if o == 'C': return 1
    if o == 'G': return 2
    if o == 'T': return 3
    if o == 0: return 'A'
    if o == 1: return 'C'
    if o == 2: return 'G'
    if o == 3: return 'T'

records = iter(handle)
record = next(records)
w,h = len(record.seq),4

r = [[0 for x in range(w)] for y in range(h)]  # Declarar matriz vaćia con las posiciones en las columnas iguales al largo de las secuencias, y los conteos de cada base en filas (que son 4).

for x in range(w):  # Llenar la matriz "r" con los conteos
    n = bXn(record.seq[x])
    r[n][x] += 1
for record in records:
    for x in range(w):
        n = bXn(record.seq[x])
        r[n][x] += 1

s = [[j[i] for j in r] for i in range(w)]  # Transpuesta de la matriz "r"

c = ''
for base_count in s:  # Encontrar un consenso
    index_min = max(range(len(base_count)), key=base_count.__getitem__)
    c += bXn(index_min)
print(c)

k = 0
for i in r:  # Imprimir la matriz del perfil
    print(bXn(k) + ': ' + ' '.join(str(x) for x in i))
    k += 1