def quicksort(array):
    if len(array) < 2: 
        return array
       # Base case: arrays with 0 or 1 element are already “sorted.” 
    else: 
         pivot = array[0] 
         less = [i for i in array[1:] if i <= pivot] 
         print(less)
         greater = [i for i in array[1:] if i > pivot]
         print(greater)
         return quicksort(less) + [pivot] + quicksort(greater) 
arr=[10, 5, 2, 3]
print(quicksort(arr))



