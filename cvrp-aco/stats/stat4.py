from graph import Graph
from ACOalgo import ACOalgo

import matplotlib.pyplot as plt
import time


# Paramètres du problème et de l'algorithme
nbr_iterations = 25
nbr_fourmis = 10

alpha = 1
beta = 2
rho = 0.5
q = 100

city_depot = 1
truck_capacity = 30







x = [ 10, 50, 100, 250, 500, 1000, 2000]
y = []


print("starting stat...")
for i, nbr_villes in enumerate(x):

    # Création du graphe
    print("loading graph...")
    graph = Graph()
    graph.generate_graph(nbr_villes, city_depot)
    print("done !")


    print(i+1,"/", len(x))
    aco = ACOalgo(graph, truck_capacity, nbr_fourmis, alpha, beta, rho, q)

    debut_timer = time.time()

    aco.lancer_algorithme(nbr_iterations)

    fin_timer = time.time()

    y.append(fin_timer - debut_timer)

    
# Tracer les courbes
plt.plot(x, y, color='blue', marker='o')

# Ajouter des labels aux axes
plt.xlabel('Nombre de villes')
plt.ylabel('Temp')

# Ajouter un titre
plt.title("Temps d'execution par rapport au nombre de villes")

# Ajouter une légende
plt.legend()

# Afficher le tableau
plt.show()
