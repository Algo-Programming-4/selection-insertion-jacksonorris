import random
arr = [random.randint(1,100) for x in range(random.randint(1,10))]

def insertion_sort(arr):   
   for x in range(len(arr)-1):      
      small = x
      
      while small > 0 and arr[small-1] > arr[small]:
        
        temp = arr[small - 1]
        arr[small - 1] = arr[small]
        arr[small] = temp

        small = small - 1
        print(arr)

print("Unsorted List: ", arr)
insertion_sort(arr)
print("Sorted List: ", arr)
