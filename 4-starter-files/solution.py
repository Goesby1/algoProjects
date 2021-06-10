# Given the reference to the head of singly LinkedList, develop an algorithm
# that detects if there exists a cycle. A cycle is defined as one of the nodes
# pointing to a previous node in the array. Thus, if we traversing the array,
# we would never know when the traversal ends.

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def hasCycle(head: Node) -> bool:
    #Empty node passed in 
    if(head is None):
        return False
    #Check at the next 3  nodes are not empty 
    if (head.next is not None and head.next.next is not None):
        pointer = head
        pointer1 = head.next.next
        
        #If there are the same then return true, this checks for a loop of size 2
        if (pointer is pointer1):
            return True
        #While they are not equal, increment pointer by 1 node and pointer1 by 2 nodes 
        while (pointer is not pointer1):
            #Repeat the process until we find the loop or we reach the end 
            if (pointer1 is None or pointer1.next is None or pointer1.next.next is None):
                break
            pointer = pointer.next
            pointer1 = pointer1.next.next
            #Return true if they are equal 
            if (pointer is pointer1):
                return True
    return False
        
     #This method a has a time complexity of k*n, depending on the size of the loop and the number of nodes, asymptotically it is O(n).
     #If there is a loop it will eventually find it. 


