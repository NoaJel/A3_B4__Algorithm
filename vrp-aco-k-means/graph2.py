import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, nombre_villes, poids_maximal):
        self.nombre_villes = nombre_villes
        self.distances = self.generate_adjacency_matrix_complete(nombre_villes, poids_maximal)
        self.depot = 0
    
    def generate_adjacency_matrix_not_complete(self, num_villes, poids_maximal, probabilite_zero):

        # Initialiser une matrice carrée de taille num_villes x num_villes avec des zéros
        adjacency_matrix = np.zeros((num_villes, num_villes), dtype=int)
        
        # Générer les poids des arêtes
        for i in range(num_villes):
            for j in range(i+1, num_villes):
                if random.random() > probabilite_zero:
                    poids = random.randint(1, poids_maximal)
                    adjacency_matrix[i][j] = poids
                    adjacency_matrix[j][i] = poids
        
        # Vérifier la connexité
        visited = [False] * num_villes
        stack = [0]
        visited[0] = True
        
        while stack:
            current = stack.pop()
            for neighbor in range(num_villes):
                if adjacency_matrix[current][neighbor] > 0 and not visited[neighbor]:
                    stack.append(neighbor)
                    visited[neighbor] = True
        
        if not all(visited):
            # Si le graphe n'est pas connexe, ajouter des arêtes supplémentaires pour le rendre connexe
            for i in range(num_villes):
                if not visited[i]:
                    poids = random.randint(1, poids_maximal)
                    j = random.choice([x for x in range(num_villes) if visited[x]])
                    adjacency_matrix[i][j] = poids
                    adjacency_matrix[j][i] = poids
        
        return adjacency_matrix

    def generate_adjacency_matrix_complete(self, nbr_villes, poids_maximal):
        # Générer une matrice carrée remplie de poids aléatoires
        matrix = np.random.randint(1, poids_maximal, (nbr_villes, nbr_villes))

        # Remplacer la diagonale par des zéros (pas de distance entre une ville et elle-même)
        np.fill_diagonal(matrix, 0)

        # Compléter la matrice en la rendant symétrique (car le graphe est complet)
        matrix = np.triu(matrix) + np.triu(matrix, 1).T

        return matrix

    def draw_graph(self):
        G = nx.from_numpy_array(self.distances)
        pos = nx.circular_layout(G)
        edge_labels = {(u, v): G.get_edge_data(u, v)['weight'] for u, v in G.edges()}
        nx.draw_networkx(G,pos=pos,with_labels=True, node_color=['lightblue'])
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
        plt.show()

    def get_distance(self, ville_depart, ville_arrivee):
        return self.distances[ville_depart][ville_arrivee]
