from pylab import *

x=-3
x2=-5

for u in range(0, 100):
    x=x + 0.06
    y=x**2
    plot(x, y, 'b*')
     
    
show()