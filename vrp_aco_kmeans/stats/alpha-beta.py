from graph import Graph
from ACOalgo import ACOalgo
import matplotlib.pyplot as plt
import numpy as np

# Paramètres du problème et de l'algorithme
nombre_villes = 980
poids_maximal = 500

nombre_iterations = 35
k_camions = 64

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

x = [ i for i in range(1, nombre_iterations+1)]
y_matrice = []

index = 0

print("starting stat...")
for a in range(1,6):

    print("for alpha :", a,"/ 5")

    for b in range(1,6):
        
        print("for beta :", b,"/ 5")

        aco = ACOalgo(graph, k_camions, alpha, beta, rho, q)

        y_matrice.append([])

        for i in range(nombre_iterations):
            print(i+1,"/",nombre_iterations)
            aco.lancer_algorithme(1)
            y_matrice[index].append(aco.cout_meilleure_solution)
        
        # Tracer les courbes
        label = 'alpha : ' + str(a) + ' beta : ' + str(b)
        plt.plot(x, y_matrice[index], label=label)

        index += 1

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