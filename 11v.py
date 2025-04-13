import heapq

def find_earliest_arrival(n, a, b, buses):
    graph = [[] for _ in range(n + 1)]  # 1-based indexing
    for u, t_start, v, t_end in buses:  # FIXED order
        graph[u].append((v, t_start, t_end))

    heap = [(0, a)]  # (arrival_time, city)
    visited = [float('inf')] * (n + 1)
    visited[a] = 0

    while heap:
        curr_time, city = heapq.heappop(heap)
        if city == b:
            return curr_time
        for neighbor, t_start, t_end in graph[city]:
            if t_start >= curr_time and t_end < visited[neighbor]:
                visited[neighbor] = t_end
                heapq.heappush(heap, (t_end, neighbor))

    return -1

# Input
n = int(input())
a, b = map(int, input().split())
m = int(input())
buses = [tuple(map(int, input().split())) for _ in range(m)]

# Output
print(find_earliest_arrival(n, a, b, buses))
