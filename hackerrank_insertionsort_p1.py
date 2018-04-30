def insertionSort1(n, arr):
    # Complete this function
    num_insert = arr[n-1]
    for num in range(n-2,-2,-1): # not includuing n-1
        if num_insert < arr[num]:
            arr[num+1] = arr[num]
            # if num == 1:
            #     arr.insert(, num_insert)
        else: # if num_insert > arr[num]
            arr[num+1] = num_insert
            #break
            return " ".join(str(e) for e in arr)
        print " ".join(str(e) for e in arr)

print insertionSort1(10, [2, 3, 4, 5, 6, 7, 8, 9, 10, 1])

