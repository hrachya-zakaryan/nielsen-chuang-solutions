from qiskit import *
import matplotlib.pyplot as plt
qx=QuantumRegister(3, 'x')
qz=QuantumRegister(2,'h')
qc=QuantumCircuit(qx,qz)
qc.cx(3,0)
qc.cx(3,1)
qc.cx(4,1)
qc.cx(4,2)
qc.draw('mpl')
plt.show()