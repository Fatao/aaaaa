from collections import deque

def is_connected(adj_matrix): # 
    n = len(adj_matrix)
    if n == 0:
        return True

    visited = [False] * n  #
    queue = deque()
    queue.append(0)
    visited[0] = True

    while queue:
        v = queue.popleft()
        for i in range(n):
            if adj_matrix[v][i] == 1 and not visited[i]:
                visited[i] = True
                queue.append(i)

    return all(visited)


def count_connected_components(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            queue = deque()
            queue.append(i)
            visited[i] = True

            while queue:
                v = queue.popleft()
                for j in range(n):
                    if adj_matrix[v][j] == 1 and not visited[j]:
                        visited[j] = True
                        queue.append(j)

            count += 1

    return count


def graph_connectivity_level(adj_matrix):
    if is_connected(adj_matrix):
        return "(степень связности 1)"
    else:
        components = count_connected_components(adj_matrix)
        return f" {components} "


# Пример использования
n = int(input())

adj_matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

result = graph_connectivity_level(adj_matrix)
print(result)


####

'''


def count_components_adj_matrix(adj_matrix, n):
    visited = [False] * n
    components = 0

    def dfs(node):
        visited[node] = True
        for neighbor in range(n):
            if adj_matrix[node][neighbor] and not visited[neighbor]:
                dfs(neighbor)

    for node in range(n):
        if not visited[node]:
            dfs(node)
            components += 1

    return components

# Ввод данных
n = int(input("Введите количество вершин: "))
adj_matrix = []

print("Введите матрицу смежности построчно (через пробел):")
for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

# Вывод результата
print("Количество компонент связности:", count_components_adj_matrix(adj_matrix, n))


'''

####








