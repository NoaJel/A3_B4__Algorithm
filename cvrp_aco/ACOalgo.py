import numpy as np
import tqdm

from cvrp_aco.ant import Ant

class ACOalgo:
    def __init__(self, graph, truck_capacity, nombre_fourmis, alpha, beta, rho, q):
        
        self.graph = graph

        self.pheromones = np.ones((graph.nbr_villes, graph.nbr_villes))                # on crée un grahe vierge pour pheromones

        self.ants = [ Ant(self.graph, truck_capacity, self.pheromones, alpha, beta) for _ in range(nombre_fourmis) ]    # on crée k fourmis avec chacune un cluster
        

        self.rho = rho
        self.q = q

        self.meilleure_solution = None
        self.cout_meilleure_solution = float('inf')
        

    def lancer_algorithme(self, nombre_iterations):
        print("##")
        print("starting ACO algorithm :")

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

        
        cout, path = min( [ (self.calculer_cout(ant.path), ant.path) for ant in self.ants] )


        if cout < self.cout_meilleure_solution:

            self.cout_meilleure_solution = cout

            self.meilleure_solution = path
    



    def calculer_cout(self, solution):
        cout = 0
        for i in range(len(solution) - 1):
            ville_depart = solution[i]
            ville_arrivee = solution[i + 1]
            cout += self.graph.get_distance(ville_depart, ville_arrivee)
        return cout

    def afficher_meilleure_solution(self):
        print("Meilleure solution trouvée :", [ i + 1 for i in self.meilleure_solution])
        print("Coût de la meilleure solution :", self.cout_meilleure_solution)

    def get_truck_paths(self):
        return self.full_path_to_truck_paths(self.meilleure_solution)

    def full_path_to_truck_paths(self, liste):
        listes_divisees = []
        sous_liste = []
        
        for element in liste:
            if element != self.graph.depot:
                sous_liste.append(element)
            elif sous_liste:
                listes_divisees.append(sous_liste)
                sous_liste = []
        
        if sous_liste:
            listes_divisees.append(sous_liste)
        
        for liste in listes_divisees:
            liste.insert(0, self.graph.depot)
            liste.append(self.graph.depot)

        return [np.array(sous_liste) for sous_liste in listes_divisees]