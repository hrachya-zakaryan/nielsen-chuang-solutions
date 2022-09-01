import numpy as np
import matplotlib.pyplot as plt

p=np.arange(0.0,1.0,0.001)
st=np.sqrt(1-2*p*(1-p))
S=-0.5*((1+st)*np.log2(0.5*(1+st))+(1-st)*np.log2(0.5*(1-st)))
H=-p*np.log2(p)-(1-p)*np.log2(1-p)

plt.plot(p,S, label="S")
plt.plot(p,H, label="H")
plt.legend()
plt.xlabel('p')
plt.ylabel('Entropy')
plt.savefig('Chapter 11/12.png')
plt.show()