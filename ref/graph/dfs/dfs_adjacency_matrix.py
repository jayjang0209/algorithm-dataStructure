# graph: adjacency matrix v by v
# Time O(V^2)
# Space O(V)
def dfs(graph, start):
    # index
    visited = [False] * len(graph)
    stack = []
    stack.append(start)

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            print(vertex)
            visited[vertex] = True
            # for neighbours
            for i in range(len(graph)):
                if graph[vertex][i] and not visited[i]:
                    stack.append(i)
    return visited

graph = [[0, 1, 1, 0], # 0-1, 0-2
         [1, 0, 1, 1], # 1-0, 1-2, 1-3
         [1, 1, 0, 0], # 2-0, 2-1
         [0, 1, 0, 0]] # 3-1
visited = dfs(graph, 0)
print(visited)