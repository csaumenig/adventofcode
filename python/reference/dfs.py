"""
Taken from: https://www.geeksforgeeks.org/dsa/depth-first-search-or-dfs-for-a-graph/
"""

def dfs_rec(adjacent: list,
            visited: list,
            start,
            resources: list):
    visited[start] = True
    resources.append(start)

    # Recursively visit all adjacent vertices
    # that are not visited yet
    for adj in adjacent[start]:
        if not visited[adj]:
            dfs_rec(adjacent, visited, adj, resources)


def dfs(adjacent:list):
    visited = [False] * len(adjacent)
    resources = []
    dfs_rec(adjacent, visited, 0, resources)
    return resources


# Driver Code Starts
def add_edge(adjacent: list,
             first,
             second):
    adjacent[first].append(second)
    adjacent[second].append(first)


if __name__ == "__main__":
    V = 5
    adj = []

    # creating adjacency list
    for i in range(V):
        adj.append([])

    add_edge(adj, 1, 2)
    add_edge(adj, 1, 0)
    add_edge(adj, 2, 0)
    add_edge(adj, 2, 3)
    add_edge(adj, 2, 4)

    # Perform DFS starting from vertex 0
    res = dfs(adj)

    for node in res:
        print(node, end=" ")