# CMPE 300 PROJECT 3 Implementation of Different Versions of Quicksort Algorithm

## Usage

- In the command prompt/terminal write this code:

 ` python3 main.py ` 

or 

Run the main.py file using your IDE.

Then it prints the algorithm version(as ver1,ver2,ver3,ver4 ), input type (as type1, type2,type3,type4) , case (worst/average) and elapsed time as output.


## Explanation of the code

Implemented every version of the four quicksort algorithm in different files:

* version1 : The classical deterministic algorithm. The pivot is chosen as the first element of the list. 
* version2 : The randomized algorithm. The pivot is chosen randomly. This is the algorithm  “Quicksort (1st version)” in the course slides
* version3 : The randomized algorithm. The list is first randomly permuted and then the classical deterministic algorithm is called where the pivot is chosen as the first element of the list.
* version4 : The deterministic algorithm. The pivot is chosen according to the “median of three”  rule.

- All of these versions works with quicksort () methods takes an array, low,high and algorithmversion parameters as input and returns sorted list. For the version3 we sent the array to second_version_quicksort() method first. This method first permutes the list and then sends it to quicksort() method.

- The implementation of the quicksort method is basically same. Only differences exist at rearrange functions since it selects the pivot element. Here the pivot selection method is determined according to the algorithm version using if else loop.

- This code is analyzing the performance of four different versions of the QuickSort algorithm by testing them on multiple input types and in both worst and average cases. The four versions of QuickSort are implemented, and the performance of each version is tested on four different input types: 1) a list of random integers between 1 and 10n, 2) a list of random integers between 1 and 0.75n, 3) a list of random integers between 1 and 0.25*n, and 4) a list of all 1's and with different array sizes. Arrays created to find the running times of algorithms are sent as parameters to quick_sort methods. For the worst case , first array is sorted then sent to algorithm. For the average case, it creates five different arrays then take the average of the execution times for each version. The function InpType determines the input type and the executiontimer function measures the running time of a given version of QuickSort on a given input list. The code then prints the performance results for each version and input type combination.

- The setrecursionlimit function is used to modify the default recursion limit set by python. Using this, we increase the recursion limit to satisfy our needs. ( Since we are using recursive quicksort algorithms )
