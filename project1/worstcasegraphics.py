# Requirements matplotlib
# you could install with this command :  pip install matplotlib

import matplotlib.pyplot as plt 
import math


# Compare the theoretical results and the actual execution times using graphs. Use graphs
# where the x-axis denotes the input size and the y-axis denotes the complexity/time.

# Worst Case Real Graph
def worstcasereal():

    # Actual execution times of W(n)
    x_worst = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_worst = [0.00000, 0.00000, 0.00099, 0.01575, 0.26797, 1.30855 , 4.22626, 21.52973, 76.90652, 209.67806]
    plt.plot(x_worst, y_worst , color = "r" ,label = "worst case real execution" )

    plt.title("Worst Case Real Execution Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()

# Worst Case Graph 1
def worstcasecomparison1():

    # Actual execution times of W(n)
    x_worst = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_worst = [0.00000, 0.00000, 0.00099, 0.01575, 0.26797, 1.30855 , 4.22626, 21.52973, 76.90652, 209.67806]
    plt.plot(x_worst, y_worst , color = "r" ,label = "worst case actual (real execution)" ) 


    #Graph of the theoretical analysis when basic operation is the operation marked as (1)
    x_cords1 = range(1,250)
    y_cords1 = [x/2 for x in x_cords1]   # theta(n)  complexity
    plt.plot(x_cords1, y_cords1, color="g" , label = "when basic operation is the operation marked as (1)" )


    plt.title("Worst Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()

# Worst Case Graph 2
def worstcasecomparison2():

    # Actual execution times of W(n)
    x_worst = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_worst = [0.00000, 0.00000, 0.00099, 0.01575, 0.26797, 1.30855 , 4.22626, 21.52973, 76.90652, 209.67806]
    plt.plot(x_worst, y_worst , color = "r" ,label = "worst case actual (real execution)" ) 


    #Graph of the theoretical analysis when basic operation is the operation marked as (2)
    x_cords1 = range(1,250)
    y_cords1 = [( (x**4)/3 + (3*(x**3))/2 + (7*(x**2))/6 )/10000000  for x in x_cords1]   # # n4/3 + 3n3/2 + 7n2/6 function complexity
    plt.plot(x_cords1, y_cords1, color="y" , label = "when basic operation is the operation marked as (2)" )


    plt.title("Worst Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()

# Worst Case Graph 3
def worstcasecomparison3():

    # Actual execution times of W(n)
    x_worst = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_worst = [0.00000, 0.00000, 0.00099, 0.01575, 0.26797, 1.30855 , 4.22626, 21.52973, 76.90652, 209.67806]
    plt.plot(x_worst, y_worst , color = "r" ,label = "worst case actual (real execution)" ) 


    #Graph of the theoretical analysis when basic operation is the operation marked as (3)
    x_cords1 = range(1,250)
    y_cords1 = [( (x**4)/3 + (3*(x**3))/2 + (7*(x**2))/6 )/10000000 for x in x_cords1]   # n4/3 + 3n3/2 + 7n2/6
    plt.plot(x_cords1, y_cords1, color="b" , label = "when basic operation is the operation marked as (3)" )


    plt.title("Worst Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()

# Worst Case Graph 4
def worstcasecomparison4():

    # Actual execution times of W(n)
    x_worst = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_worst = [0.00000, 0.00000, 0.00099, 0.01575, 0.26797, 1.30855 , 4.22626, 21.52973, 76.90652, 209.67806]
    plt.plot(x_worst, y_worst , color = "r" ,label = "worst case actual (real execution)" ) 


    #Graph of the theoretical analysis when basic operation is the operation marked as (4)
    x_cords1 = range(1,250)
    y_cords1 = [ (x**3) /100000 for x in x_cords1]   # theta ( n^3 ) function complexity
    plt.plot(x_cords1, y_cords1, color="c" , label = "when basic operation is the operation marked as (4)" )


    plt.title("Worst Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()


# Worst Case Graph 5
def worstcasecomparison5():

    # Actual execution times of W(n)
    x_worst = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_worst = [0.00000, 0.00000, 0.00099, 0.01575, 0.26797, 1.30855 , 4.22626, 21.52973, 76.90652, 209.67806]
    plt.plot(x_worst, y_worst , color = "r" ,label = "worst case actual (real execution)" ) 


    #Graph of the theoretical analysis when basic operation is the operation marked as (5)
    x_cords1 = range(1,250)
    y_cords1 = [ ( ( (x**2) + x )/2 ) /300 for x in x_cords1]   #  (n2 + n)/2
    plt.plot(x_cords1, y_cords1, color="m" , label = "when basic operation is the operation marked as (5)" )


    plt.title("Worst Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()    


worstcasereal()
worstcasecomparison1()
worstcasecomparison2()
worstcasecomparison3()
worstcasecomparison4()
worstcasecomparison5()