# A Python program for Prim's Minimum Spanning Tree (MST) algorithm. 
# The program is for adjacency matrix representation of the graph 

import sys 
def printMST(V,parent,graph): 
	print ("Edge \tWeight")
	for i in range(1, V): 
		print (parent[i], "-", i, "\t", graph[i][ parent[i] ]) 
        
def minKey(V, key, mstSet):  
	min = 10000 
	for v in range(V): 
		if key[v] < min and mstSet[v] == False: 
			min = key[v] 
			min_index = v 
	return min_index 

def primMST(V): 
    key = [10000]*V 
	 parent = [None]*V 
	 key[0] = -10
	 mstSet = [False] *V 
    parent[0] = -1 
    for cout in range(V): 
		u = minKey(V,key, mstSet)  
		mstSet[u] = True
		for v in range(V): 
			if  graph[u][v] > -10 and mstSet[v] == False and key[v] > graph[u][v]: 
				key[v] = graph[u][v] 
				parent[v] = u
    printMST(v,parent,sgraph)
graph = [ [-10, -2, -10, 6, -10], 
			[-2, -10, -3, 8, 5], 
			[-10, -3, -10, -10, 7], 
			[6, 8, -10, -10, 9], 
			[-10, 5, 7, 9, -10]] 
V=len(graph)
primMST(V); 

