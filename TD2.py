from pylab import *

x=-3
x2=-5

for u in range(0, 100):
    x=x + 0.06
    y=x**2
    plot(x, y, 'b*')

for t in range(0, 500):
    x2=x2 + 0.02
    y2=x2//2
    plot(x2, y2, 'r*')
    
show()