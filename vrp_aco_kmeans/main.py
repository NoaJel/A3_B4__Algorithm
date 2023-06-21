from vrp_aco_kmeans.graph import Graph
from vrp_aco_kmeans.ACOalgo import ACOalgo


# Paramètres du problème et de l'algorithme
nombre_villes = 3000
poids_maximal = 100

nombre_iterations = 5
k_camions = 15

alpha = 1
beta = 2
rho = 0.5
q = 100


# Création du graphe
print("create graph...")
graph = Graph(nombre_villes, poids_maximal)
print("done !")


# Création de l'algorithme ACO
print("algorithm initialization...")
aco = ACOalgo(graph, k_camions, alpha, beta, rho, q)
print("done !")

#----------------------------------------------------------#

# Exécution de l'algorithme
aco.lancer_algorithme(nombre_iterations)

# Affichage de la meilleure solution trouvée
aco.afficher_meilleure_solution()
