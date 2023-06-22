from graph import Graph
from ACOalgo import ACOalgo

import matplotlib.pyplot as plt


# Paramètres du problème et de l'algorithme
nbr_iterations = 35
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
graph.load_tsp('files/lu980.tsp', city_depot)
print("done !")


aco = ACOalgo(graph, truck_capacity, nbr_fourmis, alpha, beta, rho, q)

x = [ i for i in range(1, nbr_iterations+1)]
y1 = []
y2 = []

print("starting stat...")
for i in range(nbr_iterations):


    print(i+1,"/",nbr_iterations)
    aco.lancer_algorithme(1)
    y1.append(aco.cout_meilleure_solution)
    y2.append(aco.not_best_score)


print("camion :", len(aco.fullPath_to_truckPaths(aco.meilleure_solution)))

# Tracer les courbes
plt.plot(x, y1, label="Meilleur Chemin Global", color='orange', marker='o')
plt.scatter(x, y2, label="Meilleur Chemin Local", color='blue', marker='x')


# Ajouter des labels aux axes
plt.xlabel('Itérations')
plt.ylabel('Meilleur Chemin')

# Ajouter un titre
plt.title('Evolution du coût du meilleur chemin par itération')

# Ajouter une légende
plt.legend()

# Afficher le tableau
plt.show()
