# CMPE 300 PROJECT 1 

This project analyze the algorithm and finds the time complexity of the algorithm. It also draws the graphics of the execution times.
You should read the project1.pdf file to understand the problem.


## Usage

- In the command prompt/terminal write this code:

 ` python main.py  ` 


Note :  It will execute code in the order (Best - Average - Worst )

If You want to run each one by one , at line 150 - 151 - 152, you could make correction/you could erase .


- To view the graphic drawings execute this code :

 ` python bestcasegraphics.py  `

 ` python averagecasegraphics.py  `

 ` python worstcasegraphics.py  `

 Note :  It will draw the graphic comparisons of the best case, average case and worst case in order.


## Explanation of code

- bestcasearray(), worstcasearray() and averagecasearray() methods have been written, which takes input n , as size of the array
and returns n sized-created array.
- For bestcase all the elements in the array equals to 0.
- For worstcase all the elements in the array equals to 2.
- For average case , used the random.choices() function to get the weighted random samples i.

- Then we have implemented/converted the code which is given in the assignment to the example(arr) method
- Also implemented a timer (time.time()), to measure the operation time. It starts in the algoritm begins, ends when algorithm returns.

- Created an array for input_sizes = [1, 10, 50, 100, 200, 300, 400, 500, 600, 700]

- Lastly, implemented bestcase(), worstcase() ,averagecase() , averagecase3 methods.
- averagecase3() method runs the algorithm at least 3 times for taking the average.
- They ( bestcase(),worstcase(),averagecase() ) worked example(arr) algorithm with selected input size, with created arrays and returns the algorithm execution/running time, then prints it.

- averagecase() method does the analysis only 1 time
- averagecase3() method does the analysis 3 times and takes the average of them.