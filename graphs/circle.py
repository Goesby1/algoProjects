from collections import defaultdict

def checker(graph):
    ch = True
    print(graph)
    for x , y in graph.items():
        if(len(y) != 2):
            ch = False
            breakpoint
        else:
            for z in y :
                if (z == x):
                    ch = False
                    break
    return ch

if __name__ == "__main__":
    gr = {
        "a": ["b","a", "c"],
        "b": ["a","c"],
        "c": ["a","b"]
    }
    print(checker(gr))

#The checker takes a dictionary and checks that each key(vertex) has 2 edges and that none of the edges are leading to the the vertex itself. 
#This would confirm that the graph is a cycle graph.
#Runtime: We would have to do 2*V iterations to make sure the graph is a cycle graph, O(V*E).
#Space complexity: is constant, 1.
