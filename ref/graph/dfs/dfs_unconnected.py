def DFS(graph):
    visited = [False] * len(graph)
    for vertex in range(len(graph)):
        if not visited[vertex]:
            print("Starting traversal at vertex: ", vertex)
            dfs(graph, vertex, visited)


def dfs(graph, vertex, visited):
    visited[vertex] = True
    print(vertex) #printing the vertex being visited
    for i in range(len(graph)):
        #      connected    and    not visited
        if graph[vertex][i] and not visited[i]:
            dfs(graph, i, visited)


graph = [[0, 1, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 0],
         [0, 1, 0, 0]]

DFS(graph)