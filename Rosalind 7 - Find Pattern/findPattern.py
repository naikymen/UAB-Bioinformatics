# Hola

file = open('/home/naikymen/PycharmProjects/UAB/Bioinformatica/Rosalind 7 - Find Pattern/input2.txt')
pattern = file.readline().rstrip('\n')
secuencia = file.readline().rstrip('\n')
file.close()

lp = len(pattern)
ls = len(secuencia)

pos = []
for x in range(ls-lp+1):
    bit = secuencia[x:x+lp]
    if bit == pattern:
        pos.append(x)

print(' '.join([str(x) for x in pos]))

# http://stackoverflow.com/a/12330535