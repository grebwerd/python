def bfs(graph, root):
    visited, queue = set(), [root]
    while queue:
        vertex = queue.pop(0)
        print("The vertex is ", vertex)
        if  vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex]-visited)



if __name__ == '__main__':
    graph = {0: set([1, 2]), 1: set([2]), 2: set([])} 
    bfs(graph, 0)