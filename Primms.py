from Weighted_Graph import *

file = 'test.txt'
wg = Weighted_Graph(file)
print (wg.edge_dict())
print (wg.edge_set())
print (wg.vertex_set())
wg.draw_graph()