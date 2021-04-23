import matplotlib.pyplot as plt
import numpy as np

# sum_{n=0}^{N} 2^{-an} e^{i 2^n x},  0<a<1
N, a  = 1000, 0.5


X = np.linspace(-1,1,1000) 
Y = 0
for n in range(0,N):
    c1 = 2**(-a*n)
    Y += c1 * np.exp( 1j * (2**n) * X )

plt.plot(X,Y,'b')
plt.title("n = {}".format(N) )

plt.show()
