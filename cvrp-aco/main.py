from cvrp_aco.graph import Graph
from cvrp_aco.ACOalgo import ACOalgo

# Paramètres du problème et de l'algorithme
nbr_iterations = 1
nbr_fourmis = 10

alpha = 1
beta = 2
rho = 0.5
q = 100

city_depot = 1
truck_capacity = 30



# Création du graphe
print("loading graph...")
graph = Graph()
graph.load_tsp('files/dj38.tsp', city_depot)
print("done !")

# Création de l'algorithme ACO
print("ACO algorithm initialization...")
aco = ACOalgo(graph, truck_capacity, nbr_fourmis, alpha, beta, rho, q)
print("done !")

#----------------------------------------------------------#

while 1000000000000 < aco.cout_meilleure_solution:

    # Exécution de l'algorithme
    aco.lancer_algorithme(nbr_iterations)

    # Affichage de la meilleure solution trouvée
    aco.afficher_meilleure_solution()

    graph.draw_graph(aco.get_truck_paths())
