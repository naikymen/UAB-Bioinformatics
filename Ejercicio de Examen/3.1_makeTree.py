from Bio.Align.Applications import ClustalwCommandline
#help(ClustalwCommandline)
fasta_file = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Ejercicio de Examen/felins.fasta'
clustalw_exe = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Ejercicio de Examen/clustalw2'
clustalw_cline = ClustalwCommandline(clustalw_exe, infile=fasta_file)
import os
assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
#clustalw_cline()  # Alinear las secuencias


from Bio import AlignIO  # Importar el Alineamiento
alineamiento = AlignIO.read('felins.aln', 'clustal')


from Bio.Phylo.TreeConstruction import DistanceCalculator  # Matriz de distancias
dist_calc = DistanceCalculator('identity')
dist_matrix = dist_calc.get_distance(alineamiento)
#print(dist_matrix.names)

import csv  # Exportar la Matriz como archivo CSV
with open("dist_matrix.csv", "w") as f:
    f.write(','.join(dist_matrix.names))
    writer = csv.writer(f)
    writer.writerows(dist_matrix.matrix)

from math import log  # Para aplicar la correción de Jukes-Cantor
jc_dist_matrix = dist_matrix
for n in range(0,len(dist_matrix.matrix)-1):  # El -1 va para no tomar la primera entrada, que es un cero porque no me gusta operar sobre los ceros (?)
    jc_dist_matrix.matrix[1:][n][:-1] = [-0.75*log(1-0.75*X) for X in dist_matrix.matrix[1:][n][:-1]]  # Igual una distancia puede ser cero, pero no hay drama.
with open("dist_matrix_jc.csv", "w") as f:
    f.write(','.join(jc_dist_matrix.names))
    writer = csv.writer(f)
    writer.writerows(jc_dist_matrix.matrix)


from Bio.Phylo.TreeConstruction import DistanceTreeConstructor  # Construir el Arbol
tree_constructor = DistanceTreeConstructor(dist_calc, 'upgma')  # Armando el arbol con la calculadora de distancias anterior
tree = tree_constructor.build_tree(alineamiento)
jc_tree_constructor = DistanceTreeConstructor()  # Armado el arbol con una matriz personalizada (en este caso la coregida por Jukes-Cantor)
jc_tree = tree_constructor.upgma(jc_dist_matrix)

from Bio import Phylo
Phylo.draw(tree)
Phylo.draw(jc_tree)

'''
Info de:
http://biopython.org/wiki/Phylo
BioPython Cookbook
https://docs.python.org/3.5/library/math.html
http://stackoverflow.com/questions/6645357/doing-math-to-a-list-in-python
http://stackoverflow.com/questions/14037540/writing-a-python-list-of-lists-to-a-csv-file
'''