def bfs_paths(graph, start, goal):
    queue = [(start, [start])] #queue is a list made up of a tuple first tuple is a start and the second tuple is a list
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path): #for each next adjacency node not in the set already
            print("next is ", next)
            if next == goal: # if next equals the goal
                yield path + [next] #add the goal to the path, breaks out and returns a generator
            else:
                print("Adding the node ", next, " to the path")
                queue.append((next, path + [next]))



def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None



def main():
    graph = {'A': set(['B', 'C']), 'B': set(['A', 'D', 'E']), 'C': set(['A', 'F']), 'D': set(['B']), 'E': set(['B', 'F']), 'F': set(['C', 'E'])}
    print(shortest_path(graph, 'A','F'))

if __name__ == '__main__':
    main()