
#14(a)WAP  to represent the following graphs using a dictionary

class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, vertex, edges):
        self.graph[vertex] = edges

    def display_graph(self):
        print("Graph Representation:")
        for vertex, edges in self.graph.items():
            print(f"{vertex} -> {', '.join(map(str, edges))}")

if __name__ == "__main__":
    # Creating an instance of the Graph class
    my_graph = Graph()

    # Adding edges to the graph
    my_graph.add_edge('A', ['B','C'])
    my_graph.add_edge('B', ['D','E'])
    my_graph.add_edge('C', ['F'])
    my_graph.add_edge('D', ['C'])
    my_graph.add_edge('E', ['H'])
    my_graph.add_edge('F', [])
    my_graph.add_edge('G', [])
    my_graph.add_edge('H', [])

    # Displaying the graph
    my_graph.display_graph()
