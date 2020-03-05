# Search methods

import search

ra = search.GPSProblem('R', 'A'
                       , search.romania)
ab = search.GPSProblem('A', 'B'
                       , search.romania)
ec = search.GPSProblem('E', 'C'
                       , search.romania)
bf = search.GPSProblem('B', 'F'
                       , search.romania)

#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())
print("Ramificacion y acotación AB: ")
print(search.ram_graph_search(ab).path())
print("--------------------------")
print("Heuristica + Coste acumulado AB: ")
print(search.heuristica_graph_search(ab).path())
print("--------------------------")
print("Ramificacion y acotación RA: ")
print(search.ram_graph_search(ra).path())
print("--------------------------")
print("Heuristica + Coste acumulado RA: ")
print(search.heuristica_graph_search(ra).path())
print("--------------------------")
print("Ramificacion y acotación EC: ")
print(search.ram_graph_search(ec).path())
print("--------------------------")
print("Heuristica + Coste acumulado EC: ")
print(search.heuristica_graph_search(ec).path())
print("--------------------------")
print("Ramificacion y acotación BF: ")
print(search.ram_graph_search(bf).path())
print("--------------------------")
print("Heuristica + Coste acumulado BF: ")
print(search.heuristica_graph_search(bf).path())
print("--------------------------")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
