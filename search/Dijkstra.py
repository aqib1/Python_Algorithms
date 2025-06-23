import heapq
## Total Time Complexity: O((n + m) log n)
## Space Complexity: O(n + m)
class Dijkstra:
    def shortest_path(self, graph, start):
        shortest_dist = dict.fromkeys(graph, float('inf'))
        shortest_dist[start] = 0
        pq = [(0, start)]
        while pq:
            current_dist, current_vertex = heapq.heappop(pq)
            ## current vertex distance is already shorter
            if current_dist > shortest_dist[current_vertex]:
                continue
            ## Edge relaxation
            for neighbor, weight in graph[current_vertex]:
                sum_dist = weight + current_dist

                if sum_dist < shortest_dist[neighbor]:
                    shortest_dist[neighbor] = sum_dist
                    heapq.heappush(pq, (sum_dist, neighbor))

        return shortest_dist


if __name__ == '__main__':
    adjacency_list = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)],
        'L': [('Z', 100)]
    }
    dijkstra = Dijkstra()
    print(dijkstra.shortest_path(adjacency_list, 'A'))