import Weighted_Graph as wg

G = wg.Weighted_Graph("test.txt")

G.draw_graph()

def cost(G, e):
    return G.edge_dict()[e]


def incidentEdges(G, T):
    edges = []
    for e in G.edge_set():
        for V in T[0]:
            if V in e: 
                edges.append(e)
    return [e for e in edges if e not in T[1]]

def validIncidentEdges(G, T):
    edges = []
    for e in incidentEdges(G,T):
        if e[0] not in T[0] or e[1] not in T[0]:
            edges.append(e)  
    return edges

def minValidIncidentEdge(G, T):
    validEdges = validIncidentEdges(G, T)
    minEdge = validEdges[0]
    for e in validEdges: 
        if cost(G,e) < cost(G,minEdge):
            minEdge = e       
    return minEdge