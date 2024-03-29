graph={
    '5' : ['3','7'],
    '3' : ['2','4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
}

visited=[]
queue=[]

def bfs(visited,graph,node):
    visited.append(node);
    queue.append(node)

    while queue:
        k=queue.pop(0);
        print(k,end="")

        for neighbour in graph[k]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


#for output
print("Following is bfs search");
bfs(visited, graph, '5');