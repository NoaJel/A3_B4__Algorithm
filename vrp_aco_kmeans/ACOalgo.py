import numpy as np
from tqdm import tqdm
from sklearn.cluster import KMeans

from vrp_aco_kmeans.ant import Ant


class ACOalgo:
    def __init__(self, graph, nombre_fourmis, alpha, beta, rho, q):
        
        self.graph = graph
        self.clusters = self.clustering_algo(graph.distances, graph.depot, nombre_fourmis)   # on crée k clusters
        self.pheromones = np.ones((graph.nombre_villes, graph.nombre_villes))                # on crée un grahe vierge pour pheromones

        self.ants = [ Ant(graph, self.clusters[i], graph.depot, self.pheromones, alpha, beta) for i in range(nombre_fourmis) ]    # on crée k fourmis avec chacune un cluster
        
        self.rho = rho
        self.q = q

        self.meilleure_solution = None
        self.cout_meilleure_solution = float('inf')
        

    def lancer_algorithme(self, nombre_iterations):
        print("##")
        print("starting ACO algorithm:")

        for _ in tqdm(range(nombre_iterations)):

            self.construire_solutions()
            self.mettre_a_jour_pheromones()
            self.maj_meilleure_solution()
        
        print("done !")
        print("##")

    def construire_solutions(self):
        for ant in self.ants:
            ant.construire_chemin()

    def mettre_a_jour_pheromones(self):

        self.pheromones *= (1 - self.rho)  # évaporation

        for ant in self.ants:
            chemin = ant.path
            cout = self.calculer_cout(chemin)
            delta_pheromones = self.q / cout

            for i in range(len(chemin) - 1):
                ville_depart = chemin[i]
                ville_arrivee = chemin[i + 1]
                self.pheromones[ville_depart][ville_arrivee] += delta_pheromones

    def maj_meilleure_solution(self):

        cout_max = 0.0

        for ant in self.ants:
            chemin = ant.path
            cout = self.calculer_cout(chemin)
            cout_max += cout
        
        if cout_max < self.cout_meilleure_solution:

            self.cout_meilleure_solution = cout_max

            self.meilleure_solution = [ ant.path for ant in self.ants]

    def afficher_meilleure_solution(self):
        # print("Meilleure solution trouvée :", self.meilleure_solution)
        print("Coût de la meilleure solution :", self.cout_meilleure_solution)

    def calculer_cout(self, solution):
        cout = 0
        for i in range(len(solution) - 1):
            ville_depart = solution[i]
            ville_arrivee = solution[i + 1]
            cout += self.graph.get_distance(ville_depart, ville_arrivee)
        return cout

    def clustering_algo(self, graph, depot, n):

        print("creating clusters...")

        # Nombre de villes dans le graphe
        num_cities = graph.shape[0]

        # Effectuer le clustering
        kmeans = KMeans(n_clusters=n, n_init="auto", random_state=0)  # Nombre de clusters initialisé à 2
        kmeans.fit(graph)

        # Obtenir les labels de clustering pour chaque ville
        labels = kmeans.labels_

        # Diviser les villes en sous-ensembles en fonction des labels de clustering
        clusters = [[] for _ in range(n)]  # Nombre de clusters
        for i in range(num_cities):
            if i != depot:  # Ignorer le dépôt
                clusters[labels[i]].append(i)
        
        print("done !")

        # Retourner les sous-ensembles
        return clusters
