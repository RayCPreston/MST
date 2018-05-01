from Weighted_Graph import *

file = 'test.txt'
wg = Weighted_Graph(file)
'''print (wg.edge_dict())
print (wg.edge_set())
print (wg.vertex_set())
wg.draw_graph()
'''

edgeWeight = wg.edge_dict()
print (edgeWeight, '\n')
'''
print ('\n')
print (edgeWeight[1, 2])
print (edgeWeight[2, 3])

function to extract all weights and put into an array
weights = edgeWeight.values();
print (weights)

def findMin(arr):
    mini = arr[0]
    for i in range(len(arr)):
        if(arr[i] < min):
            mini = arr[i]
    
    return mini

min = findMin(weights)
print (mini)
'''
'''print (min(edgeWeight, key = edgeWeight.get))'''
'''
arr = [2, 4, 6]

keyMin = min(edgeWeight.keys(), key = (lambda k: edgeWeight[k]))
print(keyMin)
'''
def arrContains(val, arr):
    i = 0
    for i in range(len(arr)):
        if(arr[i] == val):
            return True
    
    return False

def addVertex(key, arr):
    i = 0
    for i in range(len(key)):
        if(arrContains(key[i], arr) == False):
            arr.append(key[i])
'''            
addVertex(keyMin, arr)

print(arr)
'''     
        
        
        
        
