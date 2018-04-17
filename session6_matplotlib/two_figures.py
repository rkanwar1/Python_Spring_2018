##################################################################
# Example:  Creating two figures in the same window
# This works largely like before, just create plt.figure(2) etc. before calling plt.show().
# Useful for interactive work; not so useful for paper-writing (use subplots for that).

import matplotlib.pyplot as plt
import numpy as np

###############################################
# Let's generate some sample data to plot
# We will plot two functions of x
pi = np.pi
npts = 64
mydt='float64'
x  = np.linspace(0,2*pi,npts,dtype=mydt)

y1 = x
y2 = x*x
y3 = np.cos(2*x)
###############################################

# Figure 1
plt.figure(1)
plt.plot(x,y1)
plt.plot(x,y2,'go')   # green circles (first letter g = green; second letter o = filled circle)
plt.plot(x,y3,'r--')  # red dashed lines (first letter r = red; second characters indicate line pattern)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot Title')

# Figure 2
plt.figure(2)
plt.plot(x,y1,'r.')   # Simple line plot
plt.plot(x,y2,'g-')   # plot
plt.plot(x,y3,'b')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Plot Title2')

# Display both figures
plt.show()



