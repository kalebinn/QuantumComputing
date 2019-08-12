from qiskit import *

q = QuantumRegister(3,'q')
qcirc = QuantumCircuit(q)

qcirc.h(q[0])
qcirc.cx(q[0],q[1]) 
qcirc.cx(q[0],q[2])

# draw the circuit
print(qcirc.draw())