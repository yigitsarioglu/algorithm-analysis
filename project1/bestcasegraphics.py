# Requirements matplotlib
# you could install with this command :  pip install matplotlib

import matplotlib.pyplot as plt 
import math


# Compare the theoretical results and the actual execution times using graphs. Use graphs
# where the x-axis denotes the input size and the y-axis denotes the complexity/time. 
# 

# Best Case Real Graph
def bestcasereal():

    
    # Actual execution times of B(n)
    x_best = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_best = [0.00000, 0.00000, 0.00000, 0.00032, 0.00222, 0.00409, 0.00886, 0.02262, 0.03970, 0.06186 ]
    plt.plot(x_best, y_best , color = "r" ,label = "best case real execution" ) 
    plt.title("Best Case Real Execution Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time (sec) ")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()

# Best Case Graph 1
def bestcasecomparison1():

    
    # Actual execution times of B(n)
    x_best = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_best = [0.00000, 0.00000, 0.00000, 0.00032, 0.00222, 0.00409, 0.00886, 0.02262, 0.03970, 0.06186 ]
    plt.plot(x_best, y_best , color = "r" ,label = "best case actual(real execution)" ) 


    #Graph of the theoretical analysis when basic operation is the operation marked as (1)
    # B(n) = theta(n) 
    x_cords1 = range(1,250)
    y_cords1 = [x/10000 for x in x_cords1]   # n  function complexity
    plt.plot(x_cords1, y_cords1, color="g" , label = "when basic operation is the operation marked as (1)" )

    plt.title("Best Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()

# Best Case Graph 2
def bestcasecomparison2():

    
    # Actual execution times of B(n)
    x_best = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_best = [0.00000, 0.00000, 0.00000, 0.00032, 0.00222, 0.00409, 0.00886, 0.02262, 0.03970, 0.06186 ]
    plt.plot(x_best, y_best , color = "r" ,label = "best case actual (real execution)" ) 


    #Graph of the theoretical analysis when basic operation is the operation marked as (2)
    # B(n) = theta(n) 
    x_cords1 = range(1,250)
    y_cords1 = [( (x*x + 2*x +1)/2 ) * (math.log(x+1) )/2000000 for x in x_cords1]   #  (n2 + 2n + 1)/2*⌈ log2(n+1) ⌉  function complexity
    plt.plot(x_cords1, y_cords1, color="y" , label = "when basic operation is the operation marked as (2)" )

    plt.title("Best Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()

# Best Case Graph 3
def bestcasecomparison3():

    
    # Actual execution times of B(n)
    x_best = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_best = [0.00000, 0.00000, 0.00000, 0.00032, 0.00222, 0.00409, 0.00886, 0.02262, 0.03970, 0.06186 ]
    plt.plot(x_best, y_best , color = "r" ,label = "best case actual (real execution)" ) 


    #Graph of the theoretical analysis when basic operation is the operation marked as (2)
    # B(n) = theta(n) 
    x_cords1 = range(1,250)
    y_cords1 = [0 for x in x_cords1]   #  0 function complexity
    plt.plot(x_cords1, y_cords1, color="b" , label = "when basic operation is the operation marked as (3)" )

    plt.title("Best Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()


 # Best Case Graph 4
def bestcasecomparison4():

    
    # Actual execution times of B(n)
    x_best = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_best = [0.00000, 0.00000, 0.00000, 0.00032, 0.00222, 0.00409, 0.00886, 0.02262, 0.03970, 0.06186 ]
    plt.plot(x_best, y_best , color = "r" ,label = "best case actual (real execution)" ) 


    #Graph of the theoretical analysis when basic operation is the operation marked as (2)
    # B(n) = theta(n) 
    x_cords1 = range(1,250)
    y_cords1 = [0 for x in x_cords1]   #  0 function complexity
    plt.plot(x_cords1, y_cords1, color="c" , label = "when basic operation is the operation marked as (4)" )

    plt.title("Best Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()   

 # Best Case Graph 5
def bestcasecomparison5():

    
    # Actual execution times of B(n)
    x_best = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_best = [0.00000, 0.00000, 0.00000, 0.00032, 0.00222, 0.00409, 0.00886, 0.02262, 0.03970, 0.06186 ]
    plt.plot(x_best, y_best , color = "r" ,label = "best case actual (real execution)" ) 


    #Graph of the theoretical analysis when basic operation is the operation marked as (2)
    # B(n) = theta(n) 
    x_cords1 = range(1,250)
    y_cords1 = [0 for x in x_cords1]   #  0 function complexity
    plt.plot(x_cords1, y_cords1, color="m" , label = "when basic operation is the operation marked as (5)" )

    plt.title("Best Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()   




bestcasereal()
bestcasecomparison1() 
bestcasecomparison2()    
bestcasecomparison3()    
bestcasecomparison4()
bestcasecomparison5()           
