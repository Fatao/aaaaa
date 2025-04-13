n = int(input())
matrix = []

for _ in range(n):
    row = input().strip()
    # Check if space-separated or not
    if ' ' in row:
        matrix.append(list(map(int, row.split())))
    else:
        matrix.append([int(c) for c in row])

# Count edges
edges = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            edges += 1

# Check if it's a complete graph (no loops, all other positions = 1)
is_full = True
for i in range(n):
    for j in range(n):
        if i != j and matrix[i][j] == 0:
            is_full = False

# Check for Eulerian cycle: in-degree == out-degree for all vertices
eulerian = True
for i in range(n):
    out_deg = sum(matrix[i])
    in_deg = sum(matrix[j][i] for j in range(n))
    if in_deg != out_deg:
        eulerian = False
        break

print(edges)
print("Полный орграф –", "Да" if is_full else "Нет")
print("Эйлерова цепь –", "Да" if eulerian else "Нет")
