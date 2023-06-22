from graph import Graph
from ACOalgo import ACOalgo

import numpy as np
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


x = [ i for i in range(1, nbr_iterations+1)]
y_matrice = []

haaa = 0

print("starting stat...")
for a in range(1,6):

    print("for alpha :", a,"/ 5")

    for b in range(1,6):

        print("for beta :", b,"/ 5")

        aco = ACOalgo(graph, truck_capacity, nbr_fourmis, a, b, rho, q)

        y_matrice.append([])

        for i in range(nbr_iterations):
            print(i+1,"/",nbr_iterations)
            aco.lancer_algorithme(1)
            y_matrice[haaa].append(aco.cout_meilleure_solution)
        
        # Tracer les courbes
        label = 'alpha : ' + str(a) + ' beta : ' + str(b)
        plt.plot(x, y_matrice[haaa], label=label)

        haaa += 1

# Ajouter des labels aux axes
plt.xlabel('Itérations')
plt.ylabel('Coûts totaux')

# Ajouter un titre
plt.title('Tableau Statistique Alpha/Beta')

# Ajouter une légende
plt.legend()

# Afficher le tableau
plt.show()

#------------------------------------------------------------#

dernieres_valeurs = [courbe[-1] for courbe in y_matrice]

# Obtenir les indices triés des dernières valeurs
indices_tries = np.argsort(dernieres_valeurs)

# Sélectionner les indices des cinq courbes ayant les dernières valeurs les plus basses
indices_cinq_plus_basses = indices_tries[:5]

# Créer une nouvelle figure pour afficher les cinq courbes sélectionnées
plt.figure()

labels = []
for i in range(5):
    for j in range(5):
        labels.append('alpha : ' + str(i+1) + ' beta : ' + str(j+1))

# Tracer les cinq courbes sélectionnées
for i in indices_cinq_plus_basses:
    plt.plot(x, y_matrice[i], label=labels[i])


# Ajouter des labels aux axes
plt.xlabel('Itérations')
plt.ylabel('Coûts totaux')

# Ajouter un titre
plt.title('Tableau Statistique Alpha/Beta')

# Ajouter une légende
plt.legend()

# Afficher le graphe
plt.show()