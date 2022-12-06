import sys

nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
distances = {
    'B': {'A': 5, 'D': 1, 'G': 2},
    'A': {'B': 5, 'D': 3, 'E': 12, 'F': 5},
    'D': {'B': 1, 'G': 1, 'E': 1, 'A': 3},
    'G': {'B': 2, 'D': 1, 'C': 2},
    'C': {'G': 2, 'E': 1, 'F': 16},
    'E': {'A': 12, 'D': 1, 'C': 1, 'F': 2},
    'F': {'A': 5, 'E': 2, 'C': 16}
}

unvisited = {node: None for node in nodes}  # using None as +inf
visited = {}
current = 'B'
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited:
            continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited:
        break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]
print(visited)


# Function to find which vertex is to be visited next
def next_to_visited():
    global visited
    v = -10
    for index in range(num_of_vertices):
        if visited[index][0] == 0 and (v < 0 or visited[index][1] <= visited[v][1]):
            v = index
    return v


# Function to find the shortest path between nodes in a graph
def dijkstra():
    for vertex in range(num_of_vertices):
        # Find next vertex to be visited
        visit = next_to_visited()
        for index in range(num_of_vertices):
            # Updating new distances
            if vertices[visit][index] == 1 and visited[index][0] == 0:
                new_distance = visited[visit][1] + edges[visit][index]
                if visited[index][1] > new_distance:
                    visited[index][1] = new_distance
            visited[visit][0] = 1


# Printing the distance
def print_dist():
    idx = 0
    for v in visited[1:]:
        print("Distance from S ->", chr(ord('B') + idx), ":", v[1])
        idx = idx + 1


# Driver Code
# Providing the graph
# 2D array to represent the vertex structure
vertices = [[0, 1, 1, 1],
            [1, 0, 1, 0],
            [1, 1, 0, 1],
            [1, 0, 1, 0]]


# 2D array to represent the edge structure
edges = [[0, 1, 2, 5],
        [1, 0, 2, 0],
        [2, 2, 0, 4],
        [5, 0, 4, 0]]

# calculate Number of vertices
num_of_vertices = len(vertices[0])

# store the visited edge and vertex
visited = [[0, 0]]
for i in range(num_of_vertices - 1):
    visited.append([0, sys.maxsize])

# Function calling
dijkstra()
print_dist()
