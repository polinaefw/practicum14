def find_shortest_distance():
    """
    Поиск кратчайшего расстояния методом перебора
    """
    N = int(input())
    M = int(input())

    graph = {}
    for _ in range(M):
        a, b, d = input().split()
        d = int(d)

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append((b, d))
        graph[b].append((a, d))

    start, end = input().split()

    visited = set()
    min_distance = [10 ** 1000]
    def dfs(current, dist):
        """
        Рекурсивная функция поиска в глубину    
        """
        if current == end:
            if dist < min_distance[0]:
                min_distance[0] = dist
            return

        visited.add(current)

        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                dfs(neighbor, dist + weight)

        visited.remove(current)

    dfs(start, 0)

    print(min_distance[0])

find_shortest_distance()
