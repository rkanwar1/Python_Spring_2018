########################################################
# Example:
#       Creating a plot with 2-D data
#       Displayed in color
#       Displayed with contours

import numpy as np
import matplotlib.pyplot as plt

#Let's create some 2-d data. 
nx = 1024
ny = 1024
mydt = 'float64'
pi = np.pi
mydata = np.zeros((nx,ny),dtype=mydt)
for i in range(nx):
    xamp = ((0.5/nx) * (nx//2-i)) **2
    for j in range(ny):
        yamp = np.cos( 2*pi*(j-ny/2)/ny)
        mydata[i,j] = xamp*yamp


################################################3
#Plot
plt.figure(1)
# We use the pcolormesh function
img = plt.pcolormesh(mydata,cmap='jet')

#If desired, we can add a colorbar
plt.colorbar(label='Amplitude')

###############################
# Add some contours
# Define the levels 
clevels = [-0.03, -0.02, -0.01, -0.005,  0.005, 0.01, 0.02, 0.03]
# We can also define line styles.  Make the negative levels dashed:
cstyles = ['--', '--', '--', '--', '-', '-', '-', '-' ]
plt.contour(mydata, levels = clevels, linestyles=cstyles)


plt.xlabel('Longitude')
plt.ylabel('Latitude')

plt.show()
