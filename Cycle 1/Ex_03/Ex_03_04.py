"""
Write a Python program to plot two or more
lines on same plot with suitable legends of each line.
"""
import matplotlib.pyplot as plt

x1 = [10,20,30]                         # line 1 points
y1 = [20,30,10]
plt.plot(x1, y1, label = "line 1")      # plotting the line 1 points 


x2 = [10,20,30]                         # line 2 points
y2 = [40,10,30] 
plt.plot(x2, y2, label = "line 2")      # plotting the line 2 points


plt.xlabel('x - axis')                  # Set the y axis label of the current axis.
plt.ylabel('y - axis')                  
plt.title('Two or more lines on same plot with suitable legends ')# Set a title 

plt.legend()                            # show a legend on the plot
plt.show()                              # Display a figure.
