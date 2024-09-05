'''
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity 
and with the smallest space complexity possible.
'''
def mergeSort(arr):

    '''
    Merge sort uses divide and conquer approach with O(nlogn) time complexity
    where logn is the level of divisions and at each level we merge n elements 
    '''
    if(len(arr) > 1):
        mid = len(arr)//2
        leftArray = arr[: mid]
        rightArray = arr[mid:]

        #divide array into sub arrays
        mergeSort(leftArray)
        mergeSort(rightArray)

        #merge sorted sub arrays
        i = 0
        j = 0
        k = 0
        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i+=1
            else:
                arr[k] = rightArray[j]
                j+=1
            k+=1

        #copy remaining left array elements
        while i < len(leftArray):
                arr[k] = leftArray[i]
                i+=1
                k+=1

        #copy remaining right array elements
        while j < len(rightArray):
                arr[k] = rightArray[j]
                j+=1
                k+=1              
    return arr

print(mergeSort([5,1,1,2,0,0]))