from graph import Graph
from ACOalgo import ACOalgo
import matplotlib.pyplot as plt
import time

# Paramètres du problème et de l'algorithme
#nombre_villes = 980
poids_maximal = 500

nombre_iterations = 35
#k_camions = 64

alpha = 1
beta = 2
rho = 0.5
q = 100

#----------------------------------------------------------#

x = [ 10, 50, 100, 250, 500, 1000, 2000, 3500, 5000]
y = []

for i in x:
    print(i+1,"/",x)

    graph = Graph(i, poids_maximal)

    aco = ACOalgo(graph, round((1/3)*i), alpha, beta, rho, q)

    debut_timer = time.time()

    aco.lancer_algorithme(nombre_iterations)
    fin_timer = time.time()
    y.append(fin_timer - debut_timer)
    
# Tracer la courbe
plt.plot(x, y, color='orange', marker='o')

# Ajouter des labels aux axes

plt.xlabel('Nombre de villes')
plt.ylabel("Temps d'éxecution (s)")

# Ajouter un titre
plt.title("Evolution du nombre de villes en fonction du temps d'éxecution")

# Ajouter une légende
plt.legend()

# Afficher le tableau
plt.show()
