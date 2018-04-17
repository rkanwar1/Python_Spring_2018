##################################################################
# Example:  Creating a plot with:
#  -- logarithmic axes
#  -- a legend
#  -- embedded latex formulae
# To begin with, we import the pyplot package from matplotlib
# Common practice is to alias pyplot as plt
# We also import numpy

import matplotlib.pyplot as plt
import numpy as np

###############################################
# Let's generate some sample data to plot
# We will plot two functions of x
pi = np.pi
npts = 64
mydt='float64'
x  = np.linspace(0.1,10,npts,dtype=mydt)

y1 = x
y2 = x*x
y3 = x*x*x
###############################################

# To create a legend, we use the label 
# keyword when creating each of our plots
# If we wish, we can use latex by setting label=r'$latex formula$'  (the r is outside the quotes)

plt.figure(1)
plt.plot(x,y1,label = 'x')
plt.plot(x,y2,'go',label = r'$x^2$'+' (with latex)') # green circles (first letter g = green; second letter o = filled circle)
plt.plot(x,y3,'r--',label=r'$x^3$'+' (with latex)')  # red dashed lines (first letter r = red; second characters indicate line pattern)

# The xlabel, ylabel, and title functions control the axes and plot title
plt.xlabel('Logarithmic x-axis')
plt.ylabel('Logarithmic y-axis')
plt.title('Plot Title')

# To use logarithmic axes, call the xscale and yscale functions and pass them the the value "log."
plt.yscale('log')
plt.xscale('log')

# Once our plot is set, call the legend function 
legend = plt.legend(loc='lower right', shadow=True, ncol = 2) 

plt.show()



