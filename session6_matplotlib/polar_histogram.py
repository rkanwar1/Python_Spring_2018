###########################################################
#
#       Plotting Example
#           - displays a histogram and a polar plot

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


###################################################
# Give the random module a random seed (optional)
np.random.seed(19680801)

npts = 512

#Random points in theta
tmean = np.pi   # mean of distribution
tsigma = np.pi# standard  deviation of the distribution
theta = tmean+tsigma*np.random.randn(npts)   # Uniformly distributed set of points

#Random points in r
rmean = 0.0     
rsigma = 1      
r = rmean + rsigma * np.random.randn(npts)

##################################################
# Ensure that r and theta have sensible values
maxr = np.max(np.abs(r))
for i in range(npts):
    theta[i] = (theta[i] % (2*np.pi))  #*180.0/np.pi

    r[i] = np.abs(r[i])/maxr
    r[i] = r[i] % 1
    



##########################################
# Begin the figure
plt.figure(1)

##############################
# Subplot 1 :  histogram of theta values
plt.subplot(1,2,1)

# the histogram of the data
num_bins = 50
plt.hist(theta, num_bins, normed=1)
plt.xlabel(r'$\theta$')
plt.ylabel('Probability density')
plt.title(r'Histogram of $\theta$-values')

################################################
# Subplot 2 : Polar Plot of our Random Points
# "ax" is an axes object.
# We can manipulate the plot via plt or else through methods of ax
ax=plt.subplot(1,2,2,projection='polar') 

for i in range(npts):
    plt.plot(theta[i], r[i], 'r.')   # plot each point individually (no connecting line)

plt.title('Random Points')
ax.set_rticks([0.5, 0.75, 1])  # Control radial ticks -- most easily accessible via "axes" object
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line

#plt.gca(projection='polar')  # If we weren't working with subplots or axes objects, we could do this

plt.tight_layout()
plt.show()
