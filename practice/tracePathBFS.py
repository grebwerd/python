from collections import deque
def bfs2(graph, start, goal):
    """
    finds a shortest path in undirected `graph` between `start` and `goal`. 
    If no path is found, returns `None`
    """
    if start == goal:
        return [start]
    visited = {start}
    queue = deque([(start, [])])

    while queue:
        current, path = queue.popleft()
        print("current is ", current, " and the path is ", path)
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == goal:
                return path + [current, neighbor]
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            print("For the neighbor", neighbor, " to the path", path, " and appending the node ", current, " to the path")
            visited.add(neighbor)   
    return None  # no path found. not strictly needed

if __name__ == '__main__':
    graph = {
        'A': set(['B', 'C']),  
        'B': set(['A', 'D', 'E']),
        'C': set(['A', 'F']),   
        'D': set(['B']),     
        'E': set(['B', 'F']),             
        'F': set(['C', 'E']),
    }
    path = bfs2(graph, 'D', 'F')
    if path:
        print(path)
    else:
        print('no path found')