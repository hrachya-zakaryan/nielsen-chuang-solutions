import qiskit
from matplotlib import pyplot as plt
from qiskit.visualization import plot_bloch_vector
from mpl_toolkits.mplot3d import Axes3D

plt.figure(figsize=(2,3))
ax=plt.subplot(2,3,1, axes_class=Axes3D)#Pauli X1
plot_bloch_vector([1,0,0], ax=ax)
ax.set_title("Pauli X",y=1.1)
ax=plt.subplot(2,3,2, axes_class=Axes3D)#Pauli Y1
plot_bloch_vector([0,1,0], ax=ax)
ax.set_title("Pauli Y",y=1.1)
ax=plt.subplot(2,3,3, axes_class=Axes3D)#Pauli Z1
plot_bloch_vector([0,0,1], ax=ax)
ax.set_title("Pauli Z",y=1.1)
ax=plt.subplot(2,3,4, axes_class=Axes3D)#Pauli X2
plot_bloch_vector([-1,0,0], ax=ax)
ax=plt.subplot(2,3,5, axes_class=Axes3D)#Pauli Y2
plot_bloch_vector([0,-1,0], ax=ax)
ax=plt.subplot(2,3,6, axes_class=Axes3D)#Pauli Z2
plot_bloch_vector([0,0,-1], ax=ax)
plt.show()
