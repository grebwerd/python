class DFS:
    

    def dfs(self, graph, start):
        visited, stack = set(), [start]
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print("Visiting vertex", vertex)
                visited.add(vertex)
                print(graph[vertex])
                print(visited)
                print(graph[vertex]-visited)
                #This adds all the nodes node visited so far the current node is connected to
                stack.extend(graph[vertex]- visited)


def main():
    graph = {'A': set(['B', 'C']), 'B': set(['A', 'D', 'E']), 'C': set(['A', 'F']), 'D': set(['B']), 'E': set(['B', 'F']), 'F': set(['C', 'E'])}
    search = DFS() 
    search.dfs(graph, 'A')




#Standard boiilerplate to call the main() function to begin
if __name__ == '__main__':
    main()