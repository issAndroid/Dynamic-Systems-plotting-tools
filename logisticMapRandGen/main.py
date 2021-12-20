# Approximations of the absolutely continuous invariant measure of the Logistic Map
import matplotlib.pyplot as plt
import numpy as np

# use x_{n1}, ..., x_{n1+N} for bar chart
n1, n2, N = 1000, 100, 1000000
x0, yp = 0.505, np.zeros(n2)

def f(x):
    return 4*x*(1-x)

# 1 / pi*sqrt( x(1-x) )  for x!=0 and x!=1
def g(x):
    b = np.sqrt(x*(1-x))*np.pi
    return(np.divide(1, b, out=np.zeros_like(b), where=b != 0))


for _ in range(n1):
    x0 = f(x0)

for _ in range(N):
    x0 = f(x0)
    m = int(np.floor(n2*x0))
    yp[m] += 1


plt.title("n2 = " + str(n2) + "   ,   N = " + str(N))
plt.xlabel(str(n2) + "*[0,1]")

# plot
xx = np.arange(0, n2+0.1, 0.1)
yy = g(xx/n2)
plt.plot(xx, yy, color='r', label="1/(pi x(1-x))")


### uncomment this part for density function
##  then comment lines 32 , 33
##for i in range(1, n2):
##    yp[i] += yp[i-1]
##yy = (0.5 + 1/np.pi * np.arcsin(2*xx/n2-1))*n2
##plt.plot(xx, yy, color='r', label="0.5 + 1/pi asin(2x-1)")


# bar plot
plt.bar(range(n2), yp/N*n2, fill=True, width=1)
plt.legend(loc="upper left")
plt.show()
