import matplotlib.pyplot as plt

from cvrp_aco.graph import Graph
from cvrp_aco.ACOalgo import ACOalgo


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
graph.load_tsp('files/dj38.tsp', city_depot)
print("done !")


x = [ i for i in range(1, nbr_iterations+1)]
y_matrice = []

print("starting stat...")
for b in range(1,6):

    print("for beta :", b,"/ 5")

    aco = ACOalgo(graph, truck_capacity, nbr_fourmis, alpha, b, rho, q)

    y_matrice.append([])

    for i in range(nbr_iterations):
        print(i + 1, "/", nbr_iterations)
        aco.lancer_algorithme(1)
        y_matrice[b - 1].append(aco.cout_meilleure_solution)
    
    # Tracer les courbes
    label = 'beta : ' + str(b)
    plt.plot(x, y_matrice[b-1], label=label)



# Ajouter des labels aux axes
plt.xlabel('Itérations')
plt.ylabel('Coûts totaux')

# Ajouter un titre
plt.title('Tableau Statistique Beta')

# Ajouter une légende
plt.legend()

# Afficher le tableau
plt.show()
