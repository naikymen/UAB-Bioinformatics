# =)

file = open('/home/naikymen/PycharmProjects/UAB/Bioinformatica/Rosalind 8 - With Tolerance/input3.txt')
pattern = file.readline().rstrip('\n')
secuencia = file.readline().rstrip('\n')
tolerancia = file.readline().rstrip('\n')
file.close()

lp = len(pattern)
ls = len(secuencia)
tol = int(tolerancia)

pos = []
for x in range(ls-lp+1):
    bit = secuencia[x:x+lp]
    k = 0
    for i,j in zip(pattern,bit):
        if i == j:
            k += 1
    if k >= lp - tol:
        pos.append(x)


print(' '.join([str(x) for x in pos]))

# http://stackoverflow.com/a/12330535