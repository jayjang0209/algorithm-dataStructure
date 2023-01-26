def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    stack.append(neighbour)
    return visited


def dfs_recursion(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            dfs_recursion(graph, neighbour, visited)
    return visited



graph = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E'])
}

visited_stack = dfs_stack(graph, 'A')
visited_recur = dfs_stack(graph, 'A')
print(visited_stack)
print(visited_recur)