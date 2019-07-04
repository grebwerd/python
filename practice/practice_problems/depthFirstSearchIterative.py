def dfs_iterative(graph, start):
    stack, path = [start], [] #use a list as a stack, path is an empty list
    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        for neighbor in graph[vertex]:
            stack.append(neighbor)
            print("The stack is ", stack)

    return path

adjacency_matrix = {10: [5, 15], 5: [2, 4],
                    2: [], 4: [3], 3:[], 15: [12,14],
                    12: [], 14: []}



def main():
    print(dfs_iterative(adjacency_matrix, 10))


if __name__ == '__main__':
    main()