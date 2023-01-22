import random
import time
from math import floor

# arr is arr[0:n-1]

def example(arr) :
    start_time = time.time() #start the time here

    arr2 = [0,0,0,0,0]    # arr2 is a list of size 5
    n = len(arr)

    for i in range (0, n-1) :
        if arr[i]==0:
            for t1 in range(i,n-1):
                p1= t1 ** 1/2
                x1 = n+1

                while x1 >=1 :
                    x1 = floor (x1 /2)
                    arr2 [i%5] = arr2 [i%5] +1
        elif arr[i]==1:

            for t2 in range(n,1, -1):
                for p2 in range(1,n):
                    x2=n+1
                    while x2>0:
                        x2= floor(x2 /2 )
                        arr2[i%5]=arr2[i%5] +1


        elif arr[i]==2:
            for t3 in range (1,n):
                x3=t3 + 1
                for p3 in range (0, (t3**2) -1 ):
                    arr2[i%5]=arr2[i%5] +1
    
       


    end_time = time.time()    #stop the time here


    execution_time=end_time - start_time
   # print (  "%.20fs" % (end_time - start_time) )
    return arr2, execution_time


#Method which produce best case input array for algorith bt making all the inputs equal to zero.
# Returns as a list
def bestcasearray(n):
    bestlist=[]

    for i in range(0,n):
        bestlist.append(0)

    return  bestlist

#Method produces worst case input array for the algorithm by making all the inputs equal to one.
#Returns as a list
def worstcasearray(n):
    worstlist=[]

    for i in range(0,n):
        worstlist.append(1)

    return  worstlist


#Produces averagecase input array- list
# Used the random.choices() function to get the weighted random samples in Python.
def averagecasearray(n):


    thelist=[]

    for i in range(0,n-1):

        list = [0, 1, 2]
        distribution = [1/3, 1/3, 1/3]

        random_number = random.choices(list, distribution)  # weighted random choices to choose from the list with different probability

        thelist.append(random_number[0])

    return thelist

   
# HERE MAIN OPERATIONS ARE DONE
# Case: xxx Size:yyy Elapsted Time: zzz
input_sizes = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
arrlen= len(input_sizes)


#Best Case Input Calculations
def bestcase ():
    for i in range (0,arrlen):

        n=input_sizes[i] # n is the input size here
        X= bestcasearray(n)   # X is the example array
        execution_time = example(X)[1]
        print( " Case: Best Size: %2d  Elapsed Time:  %.5f sec" % ( n, execution_time)   )

#Worst Case Input Calculations
def worstcase():
    for i in range (0,arrlen):

        n=input_sizes[i] # n is the input size here
        X= worstcasearray(n)   # X is the example array
        execution_time = example(X)[1]
        print( " Case: Worst Size: %2d  Elapsed Time:  %.5f sec" % ( n, execution_time)   )


#Average Case Input Calculations
def averagecase():

    for i in range (0,arrlen):

        n=input_sizes[i] # n is the input size here
        X= averagecasearray(n)   # X is the example array
        execution_time = example(X)[1]
        print( " Case: Average Size: %2d  Elapsed Time:  %.5f sec" % ( n, execution_time)   )
  
    
#In order to observe the average behavior, for each input size,  must execute the algorithm with random inputs several times and take the average.
#This method runs the code 3 times and takes the averages for each input size
#Average Case Input Calculations -run the algorithm at least 3 times for taking the average.
def averagecase3():

    for i in range (0,arrlen):
        average=0
        n=input_sizes[i] # n is the input size here

        for j in range(0,3):

            X= averagecasearray(n)   # X is the example array
            execution_time = example(X)[1]
            average = average +execution_time


        average=average/3
        print( " Case: Average Size: %2d  Elapsed Time:  %.5f sec" % ( n, average)   )



#Select which one? Best , average or worstcase scenario

bestcase()    
averagecase3()
worstcase()

#averagecase()