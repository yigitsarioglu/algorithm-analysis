# Requirements matplotlib
# you could install with this command :  pip install matplotlib

import matplotlib.pyplot as plt 
import math


# Compare the theoretical results and the actual execution times using graphs. Use graphs
# where the x-axis denotes the input size and the y-axis denotes the complexity/time. 
 
# Average Case Real Graph
def averagecasereal():


    # Actual execution times of A(n)
    x_average = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_average = [0.00000, 0.00000, 0.00057, 0.00710, 0.12868, 0.64771 , 1.74158, 9.48504, 26.22953, 70.21483]
    plt.plot(x_average, y_average , color = "r" ,label = "average case real execution" ) 
    plt.title("Average Case Real Execution Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()


# Average Case Graph 1
def averagecasecomparison1():


    # Actual execution times of A(n)
    x_average = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_average = [0.00000, 0.00000, 0.00057, 0.00710, 0.12868, 0.64771 , 1.74158, 9.48504, 26.22953, 70.21483]
    plt.plot(x_average, y_average , color = "r" ,label = "average case actual (real execution)" ) 


    #Graph of the theoretical analysis when basic operation is the operation marked as (1)
    x_cords1 = range(1,250)
    y_cords1 = [x/5 for x in x_cords1]   # theta(n)  complexity
    plt.plot(x_cords1, y_cords1, color="g" , label = "when basic operation is the operation marked as (1)" )

    plt.title("Average Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()

# Average Case Graph 2
def averagecasecomparison2():


    # Actual execution times of A(n)
    x_average = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_average = [0.00000, 0.00000, 0.00057, 0.00710, 0.12868, 0.64771 , 1.74158, 9.48504, 26.22953, 70.21483]
    plt.plot(x_average, y_average , color = "r" ,label = "average case actual (real execution)" ) 

    # n2*⌈log2(n+1)⌉/6 + n*⌈log2(n+1)⌉/6 + n3*⌈log2(n+1)⌉/3 + n4/9 + n3/2+7n2/18  complexity
    #Graph of the theoretical analysis when basic operation is the operation marked as (2)
    x_cords1 = range(1,250)
    y_cords1 = [ ( (x**2)*(math.log(x+1))/6 + x*(math.log(x+1))/6 + (x**3)*(math.log(x+1))/3 + (x**4)/9 + (x**3)/2 + (7*(x**2))/18 ) /5000000 for x in x_cords1]    # theta ( n^4 ) function complexity
    plt.plot(x_cords1, y_cords1, color="y" , label = "when basic operation is the operation marked as (2)" )

    plt.title("Average Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()

# Average Case Graph 3
def averagecasecomparison3():


    # Actual execution times of A(n)
    x_average = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_average = [0.00000, 0.00000, 0.00057, 0.00710, 0.12868, 0.64771 , 1.74158, 9.48504, 26.22953, 70.21483]
    plt.plot(x_average, y_average , color = "r" ,label = "average case actual (real execution)" ) 

    # n4/9 + n3/2 + n3*⌈ log2(n+1) ⌉/3 + 7n2/18
    #Graph of the theoretical analysis when basic operation is the operation marked as (3)
    x_cords1 = range(1,250)
    y_cords1 = [ ( (x**4)/9 + (x**3)/2 + (x**3)*(math.log(x+1))/3 + 7*(x**2)/18 )/5000000 for x in x_cords1]   # theta ( n^4 ) function complexity
    plt.plot(x_cords1, y_cords1, color="b" , label = "when basic operation is the operation marked as (3)" )

    plt.title("Average Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()


# Average Case Graph 4
def averagecasecomparison4():


    # Actual execution times of A(n)
    x_average = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_average = [0.00000, 0.00000, 0.00057, 0.00710, 0.12868, 0.64771 , 1.74158, 9.48504, 26.22953, 70.21483]
    plt.plot(x_average, y_average , color = "r" ,label = "average case actual (real execution)" ) 

    # n3/3 + n2/3
    #Graph of the theoretical analysis when basic operation is the operation marked as (4)
    x_cords1 = range(1,250)
    y_cords1 = [ ( (x**3)/3 + (x**2)/3 )/100000 for x in x_cords1]   # theta ( n^3 ) function complexity
    plt.plot(x_cords1, y_cords1, color="c" , label = "when basic operation is the operation marked as (4)" )

    plt.title("Average Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()

# Average Case Graph 5
def averagecasecomparison5():


    # Actual execution times of A(n)
    x_average = [1, 5, 10, 25, 50, 75, 100, 150, 200, 250]
    y_average = [0.00000, 0.00000, 0.00057, 0.00710, 0.12868, 0.64771 , 1.74158, 9.48504, 26.22953, 70.21483]
    plt.plot(x_average, y_average , color = "r" ,label = "average case actual (real execution)" ) 

    #(n2 + n)/6
    #Graph of the theoretical analysis when basic operation is the operation marked as (5)
    x_cords1 = range(1,250)
    y_cords1 = [ ( (x**2 + x)/6 ) /300 for x in x_cords1]  # theta ( n^2 ) function complexity
    plt.plot(x_cords1, y_cords1, color="m" , label = "when basic operation is the operation marked as (5)" )

    plt.title("Average Case Comparison Graph")    # giving a title to my graph
    plt.xlabel("input size")        # naming the x axis
    plt.ylabel("complexity/time")   # naming the y axis

    # show a legend on the plot
    plt.legend()

    plt.show()

averagecasereal()
averagecasecomparison1()
averagecasecomparison2()
averagecasecomparison3()
averagecasecomparison4()
averagecasecomparison5()