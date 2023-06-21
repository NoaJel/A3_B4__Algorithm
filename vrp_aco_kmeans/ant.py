import numpy as np

class Ant:
    def __init__(self, graph, cities, depot, pheromones, alpha, beta):
        self.graph = graph
        self.cities = cities
        self.depot = depot
        self.pheromones = pheromones

        self.alpha = alpha
        self.beta = beta

        self.path = []
        self.current_city = None
    

    def construire_chemin(self):
        self.path = [self.depot]  # Commence par le dépôt centralisé
        self.current_city = self.depot

        while len(self.path) < len(self.cities):
            prochaine_ville = self.selectionner_prochaine_ville()
            self.path.append(prochaine_ville)
            self.current_city = prochaine_ville

        # Retourne au dépôt centralisé
        self.path.append(self.depot)
        self.current_city = self.depot

    def selectionner_prochaine_ville(self):
        non_visitees = [ville for ville in self.cities if ville not in self.path]

        probabilites = self.calculer_probabilites(non_visitees)

        prochaine_ville = np.random.choice(non_visitees, p=probabilites)

        return prochaine_ville

    def calculer_probabilites(self, non_visitees):
        probabilites = []
        total = 0

        for ville in non_visitees:
            pheromone = self.pheromones[self.current_city][ville]
            distance = self.graph.distances[self.current_city][ville]
            proba = (pheromone ** self.alpha) * ((1.0 / distance) ** self.beta)
            probabilites.append(proba)
            total += proba

        probabilites = [proba / total for proba in probabilites]
        return probabilites
