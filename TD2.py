from pylab import *

a1=0
a2=0
a3=0

for u in range(0, 21):
    a1 = a1 + 2
    x=u
    y=a1
    plot(x, y, 'r*')
    
for t in range(0, 21):
    a2= a2 + 1
    x2=t
    y2=a2
    plot(x2, y2, 'b*' )
    
for w in range(0, 21):
    a3 = a3 + 0.5
    x3=w
    y3=a3
    plot(x3, y3, 'r*')
    
show()