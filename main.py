import scipy.integrate as spi
import numpy as np

def integrand(x):
    return (2*np.pi*x*(np.e**x - np.e**(-x)))

x_lower = 0  # lower limit of x
x_upper = 1  # upper limit of x



val, abserr = spi.quad(integrand, x_lower, x_upper)
print("The Volume is equal to",val)
print("\n", 4*np.pi/np.e)