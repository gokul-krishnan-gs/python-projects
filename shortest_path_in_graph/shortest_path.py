# Function to build a weighted undirected graph from user input
def build_graph():
    graph = {}

    # Keep asking until a valid integer for the number of edges is entered
    while True:
        try:
            n = int(input("Enter the number of edges in the graph: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print("\nEnter each edge in the format → source destination weight")
    print("Example: A B 5\n")

    # Input loop for all edges
    for _ in range(n):
        try:
            # Read edge details and convert weight to int
            u, v, w = input().split()
            w = int(w)
        except ValueError:
            print("Invalid input. Please enter in the format: source destination weight")
            continue

        # Add the edge u → v
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

        # Add the reverse edge v → u (since the graph is undirected)
        if v not in graph:
            graph[v] = []
        graph[v].append((u, w))  

    return graph  # Return the built graph as a dictionary


# Function to find shortest path(s) using Dijkstra's Algorithm
def shortest_path(graph, start, target=''):
    # Create a list of all nodes (unvisited)
    unvisited = list(graph)

    # Set initial distances to infinity, except the start node which is 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Initialize empty paths and set path to start node as itself
    paths = {node: [] for node in graph}
    paths[start] = [start]

    # Loop until all nodes are visited
    while unvisited:
        # Pick the unvisited node with the smallest known distance
        current = min(unvisited, key=lambda node: distances[node])

        # Check all neighbors of current node
        for neighbor, weight in graph[current]:
            # If a shorter path to neighbor is found, update it
            if distances[current] + weight < distances[neighbor]:
                distances[neighbor] = distances[current] + weight
                paths[neighbor] = paths[current] + [neighbor]

        # Mark the current node as visited by removing it from unvisited
        unvisited.remove(current)

    # If a specific target was given, print only that path
    if target:
        print(f"\nShortest path from {start} to {target}:")
        print(f"Distance: {distances[target]}")
        print("Path:", " -> ".join(paths[target]))
    else:
        # Otherwise, print shortest paths to all other nodes
        print(f"\nShortest paths from {start} to all other nodes:")
        for node in graph:
            if node == start:
                continue  # Skip the start node itself
            print(f"{start} -> {node} : Distance = {distances[node]}, Path = {' -> '.join(paths[node])}")

    # Return both the distances and paths for further use if needed
    return distances, paths


# Main Program 

# Step 1: Build the graph by taking input from the user
my_graph = build_graph()

# Step 2: Ask the user to input the starting node
start_node = input("\nEnter the starting node: ").strip()

# Step 3: Ask if the user wants to find a path to a specific target
target_choice = input("Do you want to find the path to a specific target? (y/n): ").strip().lower()

# Step 4: Based on choice, either find a single path or all paths
if target_choice == 'y':
    target_node = input("Enter the target node: ").strip()
    shortest_path(my_graph, start_node, target_node)
else:
    shortest_path(my_graph, start_node)
