from typing import Generator, Tuple


# Given a graph (undirected), determine whether or not it is a tree.
# The input will be fairly abstract as to leave the graph implementation up to the student.
# The input will have the number of nodes and then a generator* of edges.
# Nodes are numbered 0 to n-1 (inclusive).

# *you can iterate over the elements of a generator (as shown in the starter code)

# It is guaranteed that the number of vertices N <= 1e6 aka 1 million.
# The edge generator will not contain any duplicates.

# Recall that a tree is a connected acyclic graph.
# There are many equivalent definitions that will lead to different implementations.

def is_tree(n: int, edges: Generator[Tuple[int, int], None, None]) -> bool:
   
    array = [[] for _ in range(n)]
    tru = [0] * n
    ret = True

    
    for u, v in edges:
       
        if (len(array[u]) == 0 and len(array[v]) == 0 and u != v):
            array[v].append(u)
            array[u].append(v)

        else:
            if v in array[u] and u in array[v]:
                ret = False 
            elif  u != v :
                array[u].append(v)
                array[v].append(u) 
                
        
                 
                  
    for index , x in enumerate(array): 
        cnt = 0
        for y in x:
            if tru[index] == 0:
                tru[index] = 1
            if tru[y] == 1:
                cnt += 1
        if (cnt > 1):
            ret = False
    if n > 1:
        for i in tru: 
            if i == 0:
                ret = False
    elif n == 1:
        ret = True

    return ret 

#Summary: So I attempt to create a list of list where each index represents a node and the list at that index the edges. 
#         If one node or mulitple are never visited, then the graph is not a tree. If a node is visited by more than 2 nodes
#         then there exists a loop.
#Runtime: O(n^2) is the runtime since the (if x in array) function has a linear runtime. 
#Space complexity: We need a list of size n and a list of list of size n*n. So O(n^2) is the size complexity. 