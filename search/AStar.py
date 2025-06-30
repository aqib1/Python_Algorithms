import heapq
class AStar:
    def immutableStr(self):
        name = "Aqib Javed"
        name.upper()
        print(name)

    def shortest_distance(self, graph, heuristic, start, goal):
        # Store the best cost to reach each node
        visited = {}
        # Priority queue: (h(n), g(n), current_node, path_so_far)
        pq = [(heuristic[start], 0, start, [start])]

        while pq:
            h, g, current, path = heapq.heappop(pq)
            if current == goal:
                return g, path
            if current in visited and visited[current] <= g:
                continue
            visited[current] = g
            for neighbour, cost in graph[current]:
               newG = g + cost
               newH = h + heuristic.get(neighbour, float('inf'))
               heapq.heappush(pq, (newH, newG, neighbour, path + [neighbour]))

        return None, float('inf')


if __name__ == '__main__':
    graph = {
        'Arad': [('Sibiu', 140), ('Zerind', 75), ('Timisoara', 118)],
        'Zerind': [('Arad', 75), ('Oradea', 71)],
        'Oradea': [('Zerind', 71), ('Sibiu', 151)],
        'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu', 80)],
        'Timisoara': [('Arad', 118), ('Lugoj', 111)],
        'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
        'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
        'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
        'Rimnicu': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
        'Craiova': [('Drobeta', 120), ('Rimnicu', 146), ('Pitesti', 138)],
        'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
        'Pitesti': [('Rimnicu', 97), ('Craiova', 138), ('Bucharest', 101)],
        'Bucharest': []
    }

    heuristic = {
        'Arad': 366,
        'Zerind': 374,
        'Oradea': 380,
        'Sibiu': 253,
        'Timisoara': 329,
        'Lugoj': 244,
        'Mehadia': 241,
        'Drobeta': 242,
        'Craiova': 160,
        'Rimnicu': 193,
        'Fagaras': 176,
        'Pitesti': 100,
        'Bucharest': 0
    }
    aStar = AStar()
    # print(aStar.shortest_distance(graph, heuristic, 'Arad', 'Bucharest'))
    print(aStar.immutableStr())
