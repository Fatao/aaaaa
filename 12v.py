def dfs(v, visited, graph):
    visited[v] = True
    for u in range(len(graph)):
        if graph[v][u] == 1 and not visited[u]:
            dfs(u, visited, graph)

def count_connected_components(n, graph):
    visited = [False] * n
    count = 0
    for v in range(n):
        if not visited[v]:
            dfs(v, visited, graph)
            count += 1
    return count

# Normally, we'd loop over t test cases, but we'll process each test case manually here
# Read m (vertices) and s (edges)
m, s = map(int, input().split())

# Initialize m x m adjacency matrix with zeros
graph = [[0] * m for _ in range(m)]

# Read s edges and fill the adjacency matrix
for _ in range(s):
    u, v = map(int, input().split())
    # Adjust for 0-based indexing
    u, v = u - 1, v - 1
    # Undirected graph: set both directions
    graph[u][v] = 1
    graph[v][u] = 1

# Count connected components
components = count_connected_components(m, graph)

# Output "Yes" if graph is connected (1 component), "No" otherwise
print("Yes" if components == 1 else "No")