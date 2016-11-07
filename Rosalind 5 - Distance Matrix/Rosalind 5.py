from Bio import SeqIO


def hill_dist(seq_1,seq_2):
    d = 0

    for i,j in zip(seq_1,seq_2):
        if i !=j:
            d += 1

    return d


#file = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Rosalind 5 - Distance Matrix/input.fasta'
file = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Rosalind 5 - Distance Matrix/rosalind_pdst.fasta'
output = open('output','w')
records = SeqIO.parse(file,'fasta')

sequences = []
for record in records: sequences.append(record.seq)

l = len(sequences)

# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = l, l
results = [[0 for x in range(w)] for y in range(h)]

sl = len(sequences[0])

for i in range(0,l):
    for j in range(0, l):
        hd = hill_dist(sequences[i],sequences[j])
        results[i][j] = '{0:.5f}'.format(hd / sl)
        #print('{0:.3f}'.format(hd / sl))
        #https://mkaz.tech/python-string-format.html
        #http://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places

for row in results:
    print(' '.join(row))
    output.write(' '.join(row))
    output.write('\n')