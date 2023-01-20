import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits as plt_tk

# Das Volumen der Drehfiguren über die X- oder Y-Achsen.
# ist V = Integral(a,b) 2pirh dy oder dx
# 
#
#
#
#

class Shape:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.dx = 0.0
        self.dy = 0.0
        self.area = 0.0
        self.perimeter = 0.0


class Zylinder(Shape):
    def __init__(self, x, y):
        self.x = x

def equation(x, axis = 0):
    return (np.sqrt(2*x-x**2) - axis)

def Volume(equation, x1, x2):
    b = x2
    a = x1
    h = equation
    r = equation
    volume = 2 * np.pi * spi.quad(h*r, x1, x2)[0]
    return volume
print(Volume(equation, 0.0, 1.0))