import random
arr = [random.randint(1,100) for x in range(random.randint(1,10))]

def selection_sort(arr):
   
   for x in range(len(arr)-1):      
      small = x

      for i in range(x + 1, len(arr)):  
                
         if arr[i] < arr[small]:
            
            small = i  

      temp = arr[x]
      arr[x] = arr[small]
      arr[small] = temp

print("Unsorted List: ", arr)
selection_sort(arr)
print("Sorted List: ", arr)
