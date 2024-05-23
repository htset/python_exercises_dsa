import heapq

class City:
    def __init__(self, name):
        self.name = name
        self.flights = {}

class FlightGraph:
    def __init__(self):
        self.cities = {}

    #Add a city to the graph
    def add_city(self, name):
        self.cities[name] = City(name)

    #Add a flight between two cities and its cost
    def add_flight(self, src, dest, cost):
        #Assuming flights are bidirectional
        self.cities[src].flights[dest] = cost
        self.cities[dest].flights[src] = cost

    #Function to find the cheapest route between two cities
    # using Dijkstra's algorithm
    def find_cheapest_route(self, src, dest):
        dist = {city: float('inf') for city in self.cities}
        prev = {city: None for city in self.cities}
        pq = []

        dist[src] = 0
        heapq.heappush(pq, (0, src))

        while pq:
            u_dist, u = heapq.heappop(pq)

            #Process each neighbor of the current node
            for v, cost in self.cities[u].flights.items():
                if dist[u] != float('inf') and dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], v))

        #Reconstructing the path from source to destination
        path = []
        at = dest
        while at is not None:
            path.append(at)
            at = prev[at]
        path.reverse()

        return path, dist[dest]

    #Display all possible flights between two cities using DFS
    def display_all_flights(self, src, dest):
        if src not in self.cities or dest not in self.cities:
            print("Invalid cities entered.")
            return

        visited = set()
        path = [src]
        self.dfs(src, dest, visited, path)

    #Recursive DFS function to find all flights 
    # between source and destination
    def dfs(self, src, dest, visited, path):
        visited.add(src)

        if src == dest:
            self.print_path(path)
        else:
            for flight in self.cities[src].flights:
                if flight not in visited:
                    path.append(flight)
                    self.dfs(flight, dest, visited, path)
                    path.pop()

        visited.remove(src)

    #Helper function to print a path (list content)
    def print_path(self, path):
        print(" -> ".join(path))

if __name__ == "__main__":
    graph = FlightGraph()

    graph.add_city("London")
    graph.add_city("Paris")
    graph.add_city("Berlin")
    graph.add_city("Rome")
    graph.add_city("Madrid")
    graph.add_city("Amsterdam")

    graph.add_flight("London", "Paris", 100)
    graph.add_flight("London", "Berlin", 150)
    graph.add_flight("London", "Madrid", 200)
    graph.add_flight("Paris", "Berlin", 120)
    graph.add_flight("Paris", "Rome", 180)
    graph.add_flight("Berlin", "Rome", 220)
    graph.add_flight("Madrid", "Rome", 250)
    graph.add_flight("Madrid", "Amsterdam", 170)
    graph.add_flight("Amsterdam", "Berlin", 130)

    departure = input("Enter departure city: ")
    destination = input("Enter destination city: ")

    #Display all possible flights
    print(f"All possible flights between {departure} and {destination}:")
    graph.display_all_flights(departure, destination)

    #Find the cheapest route and total price
    route, total_price = graph.find_cheapest_route(departure, destination)

    #Display the cheapest route and total price
    print("Cheapest Route: " + " -> ".join(route))
    print("Total Price: " + str(total_price))
