import os

def binary(list,target):
    first=0
    last=len(list)-1
    while first<=last:
        midpoint=(first+last)//2
        
        if list[midpoint]== target:
            return midpoint
        elif list[midpoint]<target:
            first= midpoint+1
        elif list[midpoint]>target:
            last=midpoint-1
    return None

result=binary(numbers,12)
verify(result)

result=binary(numbers,6)
verify(result)

os.system("pause")