from Bio import Phylo
tree = Phylo.read('sample.dnd','newick')
print(tree)

# instalar python3-tk
# instalar matplotlib
#Phylo.draw(tree)
tree.rooted = True

tree = tree.as_phyloxml()
tree.root.color = 'red'  # gray, blue
tree.clade[0, 1].color = "blue"
#Phylo.draw(tree)


# Cargar alineamiento
from Bio import AlignIO
alineamiento = AlignIO.read('opuntia.aln', 'clustal')
print(alineamiento)

# Generar la matriz de distancias

from Bio.Phylo import TreeConstruction
print(TreeConstruction.DistanceCalculator.dna_models)
print(TreeConstruction.DistanceCalculator.protein_models)
print(TreeConstruction.DistanceCalculator.models)

distance_calc = TreeConstruction.DistanceCalculator('identity')
distance_matrix = distance_calc.get_distance(alineamiento)
print(distance_matrix)

# Construir el Arbol
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
constructor2 = DistanceTreeConstructor(distance_calc,'upgma')  # o 'nj'
tree2 = constructor2.build_tree(alineamiento)
print(tree2)
# Custom distance matrix
constructor3 = DistanceTreeConstructor()
tree3 = constructor3.upgma(distance_matrix)  # o '.nj'
print(tree3)