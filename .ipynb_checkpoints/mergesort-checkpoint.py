import os

def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer:Recursively sort the sublists created in previous steps
    Combine:Merge the sublists created in the sublists
    
    """
    
    if len(list)<=1:
        return list
    left_half, right_half=split(list)
    left=merge_sort(left_half)
    right=merge_sort(right_half)
    return merge(left,right)

def split(list):
    """
    Divide the unsorted list at the midpoint into sublists. 
    Returns two sublists - left-right
    """
    
    mid=len(list)//2
    left= list[:mid]
    right= list[mid:]
    return left, right

def merge(left, right):
    """
    Merges two sublists , sorting them in the process 
    returns a new mwerged list
    """
    l=[]
    i=0
    j=0
    
    
    while 1< len(left) and j<len(right):
        if left[i]<right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
        
    while j<len(right):
        l.append(right[j])
        j+=1
    while i< len(left):
        l.append(left[i])
        i+=1
    return l
def verify_sorted(list):
    n=len(list)
    if n==0 or n==1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])

test=[86,51,1,2,100,5,8,4,60,75]

l=merge_sort(test)
print(verify_sorted(test))
print(verify_sorted(l))
print(l)
    
os.system("pause")