#Student Name: YİĞİT SARIOĞLU
#Student Number: 2022400354
#Compile Status: Compiling
#Program Status: Working

import time
import random
import sys # importing the sys module
import copy

# the setrecursionlimit function is used to modify the default recursion limit set by python. Using this,
# we can increase the recursion limit  to satisfy our needs
 
sys.setrecursionlimit(10**9)


# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# VERSION 1
def quick_sort(array, low, high , version):

    
    # base case: if the input array has length 0 or 1, it is already sorted
    if high > low:
    # partition the array and return the position of the pivot element
        position = rearrange(array, low, high, version)
        # recursively sort the left subarray
        quick_sort(array, low, position - 1, version)
        # recursively sort the right subarray
        quick_sort(array, position + 1, high, version)
    
    

def rearrange(array, low, high, version):

    if version == 1 :
        # choose the leftmost element as the pivot
        pivotelement = array[low]
    elif version ==2 :
         # Quicksort (1st version Probabilistic algorithm) choose a random element as the pivot
        pivot_index = random.randint(low, high)
        pivotelement = array[pivot_index]
        # swap the pivot element with the leftmost element
        array[low], array[pivot_index] = array[pivot_index], array[low]
    elif version == 3 :
        # choose the leftmost element as the pivot
         pivotelement = array[low]

    elif version == 4 :
        # choose the pivot element with median of three method
        pivot_index = median_of_tree(array,low,high) 
        pivotelement = array[pivot_index]

        # swap the pivot element with the leftmost element
        array[low], array[pivot_index] = array[pivot_index], array[low]
    
    else :
        print ("Pivot should be referenced")
        return False    
    
    right = low
    left = high + 1
    while right < left:
        # move the right pointer to the right until it finds an element greater than or equal to the pivot
        right += 1
        while right < high and array[right] < pivotelement:
            right += 1
        # move the left pointer to the left until it finds an element less than or equal to the pivot
        left -= 1
        while left > low and array[left] > pivotelement:
            left -= 1
        # if the pointers have not crossed, swap the elements at their positions
        if right < left:
            array[right], array[left] = array[left], array[right]

    # put the pivot element in its correct position
    array[low], array[left] = array[left], array[low]
    # return the position of the pivot element
    return left





#Version3

#The randomized algorithm. The list is first randomly permuted and then the classical
#deterministic algorithm is called where the pivot is chosen as the first element of the
#list. This is the algorithm “Quicksort (2nd version)” in the course slides.

#“Quicksort (2st version)” in the course slides.

# version3_quicsort is the main function which permutes the list then calls the classical deterministic quicsort algorithm
def version3_quicksort(array) :
    arr = permute_list (array)
    quick_sort(arr, 0, len(arr) - 1, 3)  # calls the classical algorithm after permutation
    return arr


# Interchanges the list elements randomly
def permute_list (array) :
    n = len(array) # n is lenght of array
    for i in range(n-2) :
         index = random.randint(i, n-1) # randomly selects any index with random function
         array[i], array[index] = array[index], array[i] #interchange the list elements

    return array     



# The deterministic algorithm. The pivot is chosen according to the “median of three”  rule.
# Same algorithm with the version 1, only difference is pivot is chosen  according to the median of three rule
def median_of_tree(array,low,high):
    firstlement = array[low] # first element in the list

    secondelement = array[high] # last element in the list
    
    if len(array) % 2==1 : # odd numbered list 
        index = ( len(array) +1 ) /2   # middle number in the odd numbered list 
    else :    # even numbered list 
        index =  ( len(array) /2 )  # here we take the left side of the two numbers

    index = int (index) -1
    thirdelement = array[index]

    mylist = [firstlement,secondelement,thirdelement]
    mylist.sort()  #sorts the list
    
    median = mylist[1]
    
    if median == firstlement : 
        return low
    elif median == secondelement:
        return high    
    elif median == thirdelement:
        return index
    else :        
        return False












def InpType ( typenumber , datasize, analysecase) :
    
    n = datasize
    low_element = 1

    #InpType1. Each element of the list is an integer between 1 and 10*n.
    if typenumber == 1: 
        high_element= 10*n
    #InpType2. Each element of the list is an integer between 1 and 0.75*n
    elif typenumber == 2 :
        high_element= 0.75*n
    #InpType3. Each element of the list is an integer between 1 and 0.25*n
    elif typenumber == 3 :
        high_element= 0.25*n
    #InpType4. All the elements are the integer 1.
    elif typenumber == 4 :
        high_element = 1
    #Returns false if any other parameter comes
    else :
        return False         
    

    #WORST CASE
    if analysecase == "worst" :  # ıf worst case analyze is selected
        
        myarray = []   
        
        for i in range(n) :
            element = random.randint(low_element, high_element)
            myarray.append(element)

        myarray.sort()
    
        
        #Convert the list to a string, with hyphens as the separator
        #array_string = "-".join(str(x) for x in myarray )
        # Prints the array
        #print("Worst case array(%1d)(%5d) (%s): " %(typenumber, datasize, array_string ) )
        

        for algovers in range (1,5) :

            execution_time = executiontimer( myarray , algovers ) # Measure the execution time of the current algorithm on the current array
            print( "Algoversion: %2d Type:%2d  Case: Worst  Size: %2d  Elapsed Time:  %.5f sec" % ( algovers, typenumber, datasize, execution_time) )

       
    #AVERAGE CASE
    if analysecase == "average" :

       array1 = [random.randint(low_element, high_element) for i in range(n)]  
       array2 = [random.randint(low_element, high_element) for i in range(n)]
       array3 = [random.randint(low_element, high_element) for i in range(n)]
       array4 = [random.randint(low_element, high_element) for i in range(n)]
       array5 = [random.randint(low_element, high_element) for i in range(n)]            
       array_liste = [array1 ,array2 , array3 ,array4 ,array5]     
       
       average_execution_time = 0

       #for array in array_liste:
        #  print ("Average case array(%1d)(%5d) : " %(typenumber, datasize), array)  
      

       for algovers in range (1,5) :

          average_execution_time = 0

          for arr in array_liste :

              #print(arr)
              execution_time = executiontimer(arr , algovers ) # Measure the execution time of the current algorithm on the current array
              average_execution_time += execution_time      # Add the execution time to the total

          average_execution_time = average_execution_time / 5  # Divide the total execution time by the number of arrays to get the average

          print( "Algoversion: %2d Type:%2d  Case: Average  Size: %2d  Elapsed Time:  %.5f sec" % ( algovers, typenumber, datasize, average_execution_time) )

         




# Method which send the array as an input to the quicksort algorithm and measures the running time of the algorithm
def executiontimer( myarray , algversion) :

    arr_copy = copy.copy(myarray)

    if algversion==1:
        start_time = time.time() #start the time here
        quick_sort(arr_copy, 0, len(arr_copy) - 1, algversion)
        end_time = time.time()    #stop the time here
        execution_time=end_time - start_time
        
    elif algversion == 2:
        start_time = time.time() #start the time here
        quick_sort(arr_copy, 0, len(arr_copy) - 1, algversion)
        end_time = time.time()    #stop the time here
        execution_time=end_time - start_time

    elif algversion == 3:

        start_time = time.time() #start the time here
        version3_quicksort (arr_copy)
        end_time = time.time()    #stop the time here
        execution_time=end_time - start_time
    elif algversion == 4:
        
        start_time = time.time() #start the time here
        # print(myarray)
        quick_sort(arr_copy, 0, len(arr_copy) - 1, algversion)
        end_time = time.time()    #stop the time here
        execution_time=end_time - start_time
      
    else :
        return False

    
    return execution_time     # returns the execution time
    



         



## MAIN PART
# Running and Printing algorithms

print ("Ver1. The classical deterministic algorithm. The pivot is chosen as the first element of the list.")
print("Ver2. The randomized algorithm. The pivot is chosen randomly. This is the algorithm “Quicksort (1st version)” in the course slides.")
print ("Ver3. The randomized algorithm. This is the algorithm “Quicksort (2nd version)” in the course slides.")
print("Ver4. The deterministic algorithm. The pivot is chosen according to the “median of three” rule.")

inputlist = [100,1000,10000]  # consider three different data sizes as n=100, n=1,000, and n=10,000.

#Works average case
for i in range(1,5) :   # 1,2,3,4 as four different type number
    for j in inputlist :    # data sizes as n=100, n=1000, and n=10000.
        
    # Average case with input n
        InpType( i, j, "average")


#Works worst case
for i in range(1,5) :   # 1,2,3,4 as four different type number
   for j in inputlist :    # data sizes as n=100, n=1000, and n=10000.
        
      # Worst case with input n
      InpType( i, j, "worst")