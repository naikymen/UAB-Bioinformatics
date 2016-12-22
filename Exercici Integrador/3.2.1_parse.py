from Bio.Blast import NCBIXML

result_handle = open('/home/naikymen/PycharmProjects/UAB/Bioinformatica/Exercici Integrador/my_blast.xml')

blast_record = NCBIXML.read(result_handle)

E_VALUE_THRESH = 0.001

for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print('****Alignment****')
            print('sequence:', alignment.title)
            print('length:', alignment.length)
            print('e value:', hsp.expect)
            print('identities:', hsp.identities)
            print(hsp.query[0:75] + '...')
            print(hsp.match[0:75] + '...')
            print(hsp.sbjct[0:75] + '...')