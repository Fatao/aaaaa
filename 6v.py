#T 3



from collections import defaultdict

# Считываем количество перекрестков и дорог
n, m = map(int, input().split())

# Граф: словарь списков, где хранятся направленные дороги
graph = defaultdict(list)

# Для идентификации дорог — уникальный номер
edge_id = 0
used = dict()  # Для отслеживания, использована ли направленная дорога

# Чтение дорог, добавляем каждую в обоих направлениях
for _ in range(m):
    a, b = map(int, input().split())
    # Каждое направление получает уникальный id
    graph[a].append((b, edge_id))
    used[edge_id] = False
    edge_id += 1

    graph[b].append((a, edge_id))
    used[edge_id] = False
    edge_id += 1

path = []

# DFS, который проходит по всем направленным дорогам
def dfs(v):
    while graph[v]:
        u, eid = graph[v].pop()
        if used[eid]:
            continue
        used[eid] = True
        dfs(u)
    path.append(v)

# Запускаем обход из вершины 1
dfs(1)

# Путь нужно развернуть (так как добавляли вершины после всех вызовов)
path = path[::-1]

# Количество шагов — количество переходов
print(len(path) - 1)
# Печатаем сам маршрут
print(*path)
