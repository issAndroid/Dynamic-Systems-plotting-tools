import numpy as np
import matplotlib.pyplot as plt

n = 90

# x,y intervals
x0 ,x1 = -2.5, 2.5
y0 ,y1 = -1, 4

# function that returns dz/dt 
def F(x,y):
    return x - x*x*x/3 - y + 1.2  ,  0.08*( x + 0.7 - 0.8*y ) 


X, Y = np.meshgrid(np.linspace(x0, x1, n), np.linspace(y0, y1, n))
u, v = np.zeros_like(X), np.zeros_like(X)
NI, NJ = X.shape

for i in range(NI):
    for j in range(NJ):
        x, y = X[i, j], Y[i, j]
        u[i,j] , v[i,j] = F(x,y)


plt.streamplot(X, Y, u, v)
plt.axis([x0, x1, y0, y1])
plt.axis('square')
plt.show()

