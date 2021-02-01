import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# solve problem in [0,n] and plot it on [m,n]
n, m = 10000,900

# function that returns dz/dt
def F(z,t):
    x, y = z[0], z[1]
    return x - x*x*x/3 - y + 1.2  ,  0.08*( x + 0.7 - 0.8*y )


ts = np.linspace(0, n, n)
icx, icy = [-1], [0]

for r in icx:
    for s in icy:
        P0 = [r, s]
        Ps = odeint(F, P0, ts)
        plt.plot( Ps[:,0][m:],  Ps[:,1][m:],  color='blue' )


plt.axis('square')
plt.show()
