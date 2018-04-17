##################################################################
# Example:  Creating a plot with:
#  -- multiple subplots
#  -- text annotation
#  -- data created using an FFT

import matplotlib.pyplot as plt
import numpy as np

def compute_power(the_signal):
    """ Returns the power spectrum of the_signal 
                --Parameters--
        the_signal:  a 1-D numpy ndarray whose power spectrum is to be computed

              -- Return Values --
        the_power:  the power_spectrum of the_signal, with zero frequency stored
                    at the_power[npts//2], where npts is the size of the_signal array   
    """
    #  We use the fft function from numpy's fft package (np.fft.fft)
    the_fft = np.fft.fft(the_signal)
    # The fft returns is a complex array.   We can access the real and imaginary 
    # components of each array element using numpy's "real" and "imag" functions.
    the_power = np.real(the_fft)**2 + np.imag(the_fft)**2   

    # The FFT contains power at both negative and positive frequencies.
    # By convention, the zero-frequency-power is stored at index[0].
    # 
    # We shift the array to the right by npts//2 elements using numpy's "roll" function
    the_power = np.roll(the_power, npts//2)
    return the_power

###################################################
#  Generate some data
#  We construct three sample signals (in time) and 
#  their associated power spectrum (in frequency space)
pi = np.pi
npts = 2048
mydt='float64'
alpha = 0.50
time  = np.linspace(0,4*pi,npts,dtype=mydt)  # 512 points over the interval [0,2*pi]
dt = (np.max(time)-np.min(time))/npts
df = 1.0/dt
fshift = npts*df*0.5

frequency = np.linspace(0,npts*df,npts,dtype=mydt)
frequency = frequency-frequency[npts//2] # shift the zero point
print(frequency[ 256] )

# Let's create a few sample signals and examine their power spectrum
sig1 = np.exp(-((time-time[npts//2])/alpha)**2) # Gaussian pulse

sig2 = np.zeros(npts)  # square pulse
sig2[7*npts//16:9*npts//16] = 1.0

sig3 = sig2*np.sin(16*time)  # sine wave with square-pulse envelope

sig1_pow = compute_power(sig1)
sig2_pow = compute_power(sig2)
sig3_pow = compute_power(sig3)



plt.figure(1)

# We can place multiple plots on the same figure using the subplot function
# Prior to creating each plot, we specify it's location via three numbers
# (number of rows, number of columns, image ID; images laid out left to right and down rows)
plt.subplot(3, 2, 1)  
plt.plot(time,sig1)
plt.xlabel('time (s)')
plt.ylabel('amplitude (dB)')

# We can annotate our plot using "text"
# To do so, we specify (x-data coordinate, y-data coordinate, and string value) 
plt.text(0,0.5,'Gaussian Pulse')  # We can annotate our plot using text(x-data coord, y-data coordinate, 
plt.title('Input Signal')

plt.subplot(3,2,2)
plt.plot(frequency/1000.0,sig1_pow)
plt.xlabel('frequency (kHz)')
plt.xlim([-10,10])
plt.title('Power Spectrum')

plt.subplot(3, 2, 3)
plt.plot(time,sig2)
plt.xlabel('time (s)')
plt.ylabel('amplitude (dB)')
# We can add a bounding box around our annotation if we would like
# using the 
# alpha = 0 is transparent; alpha = 1 is opaque
plt.text(0,0.5,'Square Pulse', bbox=dict(facecolor='red', alpha=0.1))  

plt.subplot(3,2,4)
plt.plot(frequency/1000.0,sig2_pow)
plt.xlabel('frequency (kHz)')
plt.xlim([-10,10])

plt.subplot(3, 2, 5)
plt.plot(time,sig3)
plt.xlabel('time (s)')
plt.ylabel('amplitude (dB)')
plt.text(0,0.5,'Truncated Sine Wave')

plt.subplot(3,2,6)
plt.plot(frequency/1000.0,sig3_pow)
plt.xlabel('frequency (kHz)')
plt.xlim([-10,10])

plt.tight_layout()   # This command can be 
plt.show()
