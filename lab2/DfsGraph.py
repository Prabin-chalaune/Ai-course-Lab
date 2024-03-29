#Q. DFS
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
                print(f"{start_node} -> {end_node}, Path Distance: {distance} km")


    def DFS(self, start_node, end_node, visited=None, path=None, total_distance=0):

        if visited is None:
            visited = set();
        if path is None:
            path = [];

        path.append(start_node)
        visited.add(start_node)

        if start_node == end_node:
            print("Path from Biratnagar to Damak: ", ' -> '.join(path))
            print("Total Distance:", total_distance, "km")
            return

        if start_node in self.graph:
            for neighbor, distance in self.graph[start_node].items():
                if neighbor not in visited:
                    self.DFS(neighbor, end_node, visited, path, total_distance + distance)
        path.pop()

if __name__ == "__main__":
    my_graph = Graph()
    my_graph.add_edge('Biratnagar', [['Itahari', 22], ['Biratchowk', 30], ['Rangeli', 25]])
    my_graph.add_edge('Itahari', [['Biratchowk', 11], ['Dharan', 20]])
    my_graph.add_edge('Rangeli', [['Kanepokhari', 25], ['Urlabari', 40]])
    my_graph.add_edge('Biratchowk', [['Kanepokhari', 150]])
    my_graph.add_edge('Kanepokhari', [['Urlabari', 12],['Rangeli', 25]])
    my_graph.add_edge('Urlabari', [['Damak', 6]])

    my_graph.display_graph()

    my_graph.DFS('Biratnagar', 'Damak')


