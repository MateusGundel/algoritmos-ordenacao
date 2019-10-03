def insertionSort(items): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(items)): 
  
        key = items[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < items[j] : 
                items[j+1] = items[j] 
                j -= 1
        items[j+1] = key

        return items