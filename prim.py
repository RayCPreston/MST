from func import G
import func as P

V = G.vertex_set()

def Prims(Graph,initialVertex):
    

    VT = {initialVertex} 
    ET = [] 
    MST = (VT, ET) 
    
    costMinEdge=P.cost(G,P.minValidIncidentEdge(G,MST))
    
    while MST[0] != V:
        minEdge = P.minValidIncidentEdge(G,MST)
        newVertex = {minEdge[0], minEdge[1]}
        
        ET.append(minEdge)
        MST =[newVertex.union(MST[0]),ET]
    print('MST:',MST, '\n')
    
    totalCost =0
    for e in MST[0]:
        totalCost += costMinEdge
    print ('\n', 'Total cost of MST:', totalCost, '\n')
        
       
    G.draw_subgraph(MST)
