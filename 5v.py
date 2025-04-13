# Read number of vertices and edges
n, m = map(int, input().split())

# Read all edges
edges = []
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))

# Initialize parent array
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

# Find function
def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

# Union function
def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a
        return True
    return False

# Build tree
tree = []
for u, v in edges:
    if union(u, v):
        tree.append((u, v))
    if len(tree) == n - 1:
        break

# Output result
for u, v in tree:
    print(u, v)
