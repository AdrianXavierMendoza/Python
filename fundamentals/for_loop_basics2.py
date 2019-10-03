#1 Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
def biggie(arr):
    for i in range(0,len(arr),1):
        if(arr[i]>0):
            arr[i] = 'big'
    return arr
print(biggie([1,-4,0,6,-3]))

#2 Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values.
def count(arr):
    count=0
    for i in range(0,len(arr),1):
        if(arr[i]>0):
            count+=1
    arr[len(arr)-1] = count
    return arr
print(count([1,4,0,6,-8]))

#3 Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
def sum(arr):
    sum = 0
    for i in range(0,len(arr),1):
        sum+=arr[i]
    return sum
print(sum([1,2,3,4,5]))

#4 Average - Create a function that takes a list and returns the average of all the values.
def average(arr):
    sum = 0
    for i in range(0,len(arr),1):
        sum+=arr[i]
    return (sum/len(arr))
print(average([1,2,3,4,5]))

#5 Length - Create a function that takes a list and returns the length of the list.
def length(arr):
    return len(arr)
print(length([1,2,3,4,5]))

#6 Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(arr):
    return min(arr)
print(minimum([4,-3,0,7,-6]))

#7 Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
def maximum(arr):
    return max(arr)
print(maximum([4,-3,0,7,-6]))

#8 Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
import statistics
def ultimate(arr):
    return "sumTotal:", sum(arr), "max:", max(arr), "min:", min(arr),"avg:", statistics.mean(arr)
print(ultimate([37,2,1,-9]))

#9 Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list.
def revList(arr):
    for i in range(int(len(arr)/2)):
        temp = arr[i]
        arr[i] = arr[len(arr)-(i+1)]
        arr[len(arr)-(i+1)] = temp
    return arr
print(revList([1,2,3,4,5]))