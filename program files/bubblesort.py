import random 
import time

arr=[]
for i in range(99):
    ele=random.randint(1,100)
    arr.append(ele)

newarr=[]

def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

            print(arr)

    return arr


print(arr)

print("this is the sorted array ",bubblesort(arr))

# print("this is sorted using sortng algo method ",sortingALGO(arr,newarr))


