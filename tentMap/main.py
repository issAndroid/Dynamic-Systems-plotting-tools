import matplotlib.pyplot as plt
import numpy as np

# initial point
x0 = 2
x  = np.linspace(1,2.5,100)

def f(x):
    return 2 * x**2 / ( 1 + x**2 )


y = x
plt.plot(x, y,    color='blue')
plt.plot(x, f(x), color='red')

xn = [x0]
for i in range(100):
    xn.append( f(xn[i]) )

for i in range(100):
    if (xn[0] > 3):
        break
    plt.plot( [xn[i], xn[i]],   [xn[i], xn[i+1]]   ,color='black' )
    plt.plot( [xn[i+1], xn[i]], [xn[i+1], xn[i+1]] ,color='black' )


plt.axis('square')
plt.show()
