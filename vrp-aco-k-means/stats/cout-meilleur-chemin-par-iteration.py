from graph import Graph
from ACOalgo import ACOalgo
import matplotlib.pyplot as plt

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
y1 = []
y2 = []

for i in range(nombre_iterations):
    print(i+1,"/",nombre_iterations)
    aco.lancer_algorithme(1)
    y1.append(aco.cout_meilleure_solution)
    y2.append(aco.cout_not_meilleure)

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