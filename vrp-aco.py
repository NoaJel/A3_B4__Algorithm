import numpy as np


n_cities = 1500 # Number of cities
cities = np.random.randint(1, 101, size=(n_cities, n_cities)) # Initizaliting adjcency matrix with weight from 1 to 100 and n cities

def ant_colony_optimization_vrp(cities, n_ants, n_iterations, alpha, beta, evaporation_rate, Q, n_trucks):
    '''
    ACO for Vehicle Routing Problem.
    Parameters:
        cities: 2D array of distances between cities (adjacency matrix)
        n_ants: Number of ants running per iteration
        n_iterations: Number of iterations
        alpha: Importance of pheromone
        beta: Importance of distance
        evaporation_rate: Rate at which pheromone evaporates
        Q: Constant for pheromone update / Amount of pheromones ants release
        n_trucks: Number of trucks available
    Returns:
        best_paths: List of best paths found by the algorithm
        best_total_length: Total length of the best paths

    adapted the source code for our purpose (no coordinate/matplotlib in our version and added truck constraint)
    source: https://induraj2020.medium.com/implementation-of-ant-colony-optimization-using-python-solve-traveling-salesman-problem-9c14d3114475

    '''
    pheromone = np.ones((n_cities, n_cities)) # Initizaliting pheromone matrix with 1s
    best_paths = None 
    best_total_length = np.inf
    max_cities_per_truck = n_cities // n_trucks  # Maximum cities each truck can visit

    for _ in range(n_iterations):
        all_paths = []
        all_total_lengths = []

        for _ in range(n_ants):
            paths = []
            total_length = 0
            visited_global = np.zeros(n_cities, dtype=bool)  # Global visited array for all trucks in this iteration (filled with False)

            for _ in range(n_trucks):
                visited = visited_global.copy()  # Using the global visited array for each truck
                current_point = 0  # Start from the depot
                # start from depot and visit max_cities_per_truck cities
                visited[current_point] = True 
                path = [current_point]
                path_length = 0
                cities_visited = 0  # Count of visited cities

                # Loop through not visited cities
                while np.any(np.logical_not(visited)) and cities_visited < max_cities_per_truck :
                    unvisited = np.where(np.logical_not(visited))[0] # getting the next unvisited cities
                    # calculating the probabilities of the next cities
                    probabilities = pheromone[current_point][unvisited]**alpha * (1/cities[current_point][unvisited])**beta
                    # if all the probabilities are 0, set them to 1/len(probabilities) to avoid division by 0
                    if np.sum(probabilities) == 0:
                        probabilities = np.ones_like(probabilities) / len(probabilities)
                    else:
                        probabilities /= np.sum(probabilities) # normalizing the probabilities

                    next_point = np.random.choice(unvisited, p=probabilities) # choosing the next city based on the probabilities
                    path.append(next_point)
                    path_length += cities[current_point][next_point]
                    visited[next_point] = True
                    visited_global[next_point] = True  # Mark city as visited in the global array
                    current_point = next_point
                    cities_visited += 1  # Increase the count of visited cities

                path_length += cities[path[-1]][0] # adding the distance from the last city to the depot
                path.append(0) # adding the depot to the path to complete the cycle
                paths.append(path)
                total_length += path_length

            all_paths.append(paths)
            all_total_lengths.append(total_length)

            if total_length < best_total_length:
                best_paths = paths
                best_total_length = total_length

        pheromone *= evaporation_rate # Evaporate pheromone

        for paths, total_length in zip(all_paths, all_total_lengths):
            for path in paths:
                pheromone[path[:-1], path[1:]] += Q / total_length # Update pheromone
                pheromone[path[-1], path[0]] += Q / total_length # Update pheromone

    return best_paths, best_total_length # Return the best paths and the total length of the best paths

# adjust the parameters to get the best result (add ants/iterations for precision (but slower) and increase alpha/beta for exploration)
best_paths, best_total_length = ant_colony_optimization_vrp(cities, n_ants=10, n_iterations=40, alpha=2, beta=2, evaporation_rate=0.4, Q=70, n_trucks=3)

# showing the best path and distance for each truck
total_dist = 0
for i, path in enumerate(best_paths): # Loop through the best paths
    path_distance = 0
    for j in range(len(path) - 1):
        distance = cities[path[j]][path[j+1]]
        path_distance += distance
        total_dist+= distance
    print(f"Truck {i+1}: {path} {path_distance}km")

print(f"total distance: {total_dist}km")
