import matplotlib.pyplot as plt

# set initial point and interval for r
x_0, r_0, r_1, n = 0.02, 2, 4, 1000


## r_points is x Axis points
dr = (r_1-r_0) / n
X_plot, Y_plot = [], []
r_points = []
for i in range(n):
    r_points.append( r_0 + (1 + i)*dr )

## define f(x,dr) and x(n,dr)
#  f(x,dr) is target function depended on dr
#  x50(dr) returns {x_50, ... ,x_100}, where x_(i+1) = f(x_i, dr) , x_0 is readed x_0
def f(x,r):
    return r*x*(1-x)

def getX_50(r):
    x = x_0
    for i in range(50):
        x = f(x,r)
    return x

def get50(r):
    buffer = []
    buffer.append( getX_50(r) )
    for i in range(50):
        buffer.append(f(buffer[i],r))
    return buffer 

for r in r_points:
    for x in get50(r):
        X_plot.append(r)
        Y_plot.append(x)

plt.scatter(X_plot, Y_plot, color= 'blue', marker= ".", s=10) 
# free memory
X_plot, Y_plot = [], []
plt.show()
