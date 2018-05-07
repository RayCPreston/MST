from prim import Prims
from func import G

#from prim import V
#import random

#initialVertex = random.choice(V)

initialVertex = int(input('Enter an arbitrary vertex for Prims Algorithm: ' ))

Prims(G, initialVertex)
