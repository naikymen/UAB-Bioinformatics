from Bio.Align.Applications import ClustalwCommandline
#help(ClustalwCommandline)
fasta_file = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Ejercicio de Examen/felins.fasta'
clustalw_exe = '/home/naikymen/PycharmProjects/UAB/Bioinformatica/Ejercicio de Examen/clustalw2'
clustalw_cline = ClustalwCommandline(clustalw_exe, infile=fasta_file)
import os
assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
clustalw_cline()  # Alinear las secuencias


from Bio import AlignIO  # Importar el Alineamiento
alineamiento = AlignIO.read('felins.aln', 'clustal')


from Bio.Phylo.TreeConstruction import DistanceCalculator  # Matriz de distancias
dist_calc = DistanceCalculator('identity')
dist_matrix = dist_calc.get_distance(alineamiento)
#print(dist_matrix)


from Bio.Phylo.TreeConstruction import DistanceTreeConstructor  # Construir el Arbol
tree_constructor = DistanceTreeConstructor(dist_calc, 'upgma')
tree = tree_constructor.build_tree(alineamiento)

from Bio import Phylo
Phylo.draw(tree)

'''
Info de:
http://biopython.org/wiki/Phylo
BioPython Cookbook
'''