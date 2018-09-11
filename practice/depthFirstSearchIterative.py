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

adjacency_matrix = {1: [2, 3], 2: [4, 5],
                    3: [5], 4: [6], 5: [6],
                    6: [7], 7: []}

def main():
    print(dfs_iterative(adjacency_matrix, 1))


if __name__ == '__main__':
    main()