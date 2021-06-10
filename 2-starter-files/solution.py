# Given an array of size n, where the values are between 1 and n inclusive and
# each value may at most appear twice, return a List of all the duplicate
# elements. All tests have duplicates occur in ascending order (i.e. a duplicate
# 1 would occur before a duplicate 2, etc), so your output MUST have the
# duplicates in ascending order!


from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    #Create a list of size n with 0 values and another that is empty 
    chkList = [0] * nums.__len__()
    retList = []
    #initialize a counter
    cntr = 1
    #Go through the checker list and for each value in nums increment the value in chkList by 1
    #If a number shows duplicated then it's value is 2 by the end of this process 
    for x in nums:
        chkList[x - 1] = chkList[x-1] + 1
    #Now if the value at chkList is 2, then it is a dulplicate and should be added to the list
    for x in chkList:
        if x == 2:
            retList.append(cntr)
        #increment by 1
        cntr = cntr + 1
    return retList
#This algorithm uses a checker to keep track of duplicates, then uses a loop to see which values are duplicated. If the indexed value is equal to 2 then we add it to the return list. 
#This algorithm has a space complexity of O(n) since we need to create a array of size n. 
#The time complexity is linear, O(n).                       

