import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# Define the VRP class
class VRP:
    def __init__(self, num_vehicles, num_nodes, distances):
        self.num_vehicles = num_vehicles
        self.num_nodes = num_nodes
        self.distances = distances

    def initialize_solution(self):
        customers = list(range(1, self.num_nodes))  # Exclude the warehouse (node 0)
        np.random.shuffle(customers)
        solution = [[] for _ in range(self.num_vehicles)]

        for customer in customers:
            vehicle_index = customer % self.num_vehicles
            solution[vehicle_index].append(customer)

        # Ensure each vehicle starts and ends at the warehouse (node 0)
        for route in solution:
            route.insert(0, 0)
            route.append(0)

        return solution

    def evaluate_solution(self, solution):
        total_distance = 0

        for route in solution:
            route_distance = sum(self.distances[route[i]][route[i+1]] for i in range(len(route) - 1))
            total_distance += route_distance

        return total_distance

    def generate_neighbors(self, solution):
        neighbors = []

        for vehicle_index, route in enumerate(solution):
            for i in range(1, len(route) - 1):  # Exclude the warehouse (node 0)
                for j in range(i + 1, len(route) - 1):  # Exclude the warehouse (node 0)
                    neighbor = [route[:] for route in solution]
                    neighbor[vehicle_index][i], neighbor[vehicle_index][j] = neighbor[vehicle_index][j], neighbor[vehicle_index][i]
                    neighbors.append(neighbor)

        return neighbors

    def tabu_search(self, max_iterations, tabu_list_size):
        current_solution = self.initialize_solution()
        best_solution = current_solution
        tabu_list = []

        for _ in range(max_iterations):
            neighbors = self.generate_neighbors(current_solution)
            best_neighbor = None
            best_neighbor_distance = float('inf')

            for neighbor in neighbors:
                neighbor_distance = self.evaluate_solution(neighbor)

                if neighbor_distance < best_neighbor_distance and neighbor not in tabu_list:
                    best_neighbor = neighbor
                    best_neighbor_distance = neighbor_distance

            if best_neighbor is None:
                break  # No improving neighbors found

            current_solution = best_neighbor
            tabu_list.append(best_neighbor)
            if len(tabu_list) > tabu_list_size:
                tabu_list = tabu_list[1:]  # Remove oldest move from Tabu list

            if self.evaluate_solution(current_solution) < self.evaluate_solution(best_solution):
                best_solution = current_solution

        return best_solution

def main():
    def generate_matrix(node_number):
        G = nx.complete_graph(node_number)
        for u, v in G.edges():
            G.edges[u,v]['weight'] = np.random.randint(1, 25)
        return nx.to_numpy_array(G, dtype=np.int32) # matrix

    def draw_graph(matrix):
        G = nx.from_numpy_array(matrix)
        pos = nx.spring_layout(G)
        edge_labels = { (u, v): G.get_edge_data(u, v)['weight'] for u, v in G.edges() }
        nx.draw_networkx(G,pos=pos,with_labels=True, node_color=['lightblue'])
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, bbox=dict(facecolor='white', edgecolor='none', alpha=0.7))
        plt.show()
    
    num_vehicles = 3
    num_customers = 18
    distances = generate_matrix(num_customers)
    
    vrp = VRP(num_vehicles, num_customers, distances)
    
    best_solution = vrp.tabu_search(max_iterations=100, tabu_list_size=10)
    print(f"Best solution: {best_solution}")
    print(f"Distances matrix: {distances}")
    print("Graph:")
    draw_graph(distances)


if __name__ == "__main__":
    main()
