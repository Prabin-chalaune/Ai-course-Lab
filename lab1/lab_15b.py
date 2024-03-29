
#14(b)Wap to resent the following graph using a dictionary
class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, start_node, edges):
        if start_node not in self.graph:
            self.graph[start_node] = {}
        for end_node, distance in edges:
            self.graph[start_node][end_node] = distance
    def display_graph(self):
        print("Graph Representation:")
        for start_node, connections in self.graph.items():
            for end_node, distance in connections.items():
                print(f"{start_node} -> {end_node}, Distance: {distance} km")


if __name__ == "__main__":
    # Creating an instance of the Graph class
    my_graph = Graph()
    # Adding edges and distances to the graph
    my_graph.add_edge('Biratnagar', [['Itahari', 22], ['Biratchowk', 30], ['Rangeli', 25]])
    my_graph.add_edge('Itahari', [['Biratchowk', 11], ['Dharan', 20]])
    my_graph.add_edge('Rangeli', [['Kanepokhari', 25], ['Urlabari', 40]])
    my_graph.add_edge('Biratchowk', [['Kanepokhari', 150]])
    my_graph.add_edge('Kanepokhari', [['Urlabari', 12]])
    my_graph.add_edge('Urlabari', [['Damak', 6]])

    # Displaying the graph with distances
    my_graph.display_graph()
