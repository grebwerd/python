def bfs_iterative(graph, start):
    queue, path = [start], []
    while queue:
        vertex = queue.pop(0)
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            queue.append(neighbor)
            print("The path is ", queue)

    return path


def main():
    adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}
    print(bfs_iterative(adjacency_matrix, 1))

if __name__ == '__main__':
    main()