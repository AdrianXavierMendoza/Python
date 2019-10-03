#1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    for x in range(num, -1, -1):
        print (x)
countdown (5)

#2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def printReturn(arr):
    print(arr[0])
    return arr[1]
print (printReturn([1,4]))

#3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first(arr):
    return arr[0]+len(arr)
print(first([2,3,0,-1,6]))

#4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def second(arr):
    newarr = []
    if(len(arr)<2):
        return False
    else:
        for i in range(0, len(arr), 1):
            if(arr[i]>arr[1]):
                newarr.append(arr[i])
    return newarr
print (second([2,2,-1,0,8]))
print (second([9]))

#5 This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length(s,v):
    arr = []
    for i in range(0,s,1):
        arr.append(v)
    return arr
print(length(5,9))