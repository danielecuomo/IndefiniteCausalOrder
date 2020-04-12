#!/usr/bin/env python
# coding: utf-8

#Create a parametrized gate implementing a quantum switch.
#input D, E are Gate objects 
#qubit 0 is the target.
#qubit 1 is an ancilla gate, therefore it will be reset to state |+>.

from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info import Operator

def OneQubitSwitchGate(D, E):
    switch = QuantumCircuit(2, name='$\mathcal{S}$')
    
    Dmat = D.to_matrix()
    cD = Operator([[Dmat[0][0], Dmat[0][1], 0, 0],
                   [Dmat[1][0], Dmat[1][1], 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]])

    switch.reset(1)
    switch.h(1)
    switch.x(1)
    switch.unitary(cD, [1, 0], 'D')
    switch.x(1)
    switch.barrier()
    switch.append(E, 0)
    switch.unitary(cD, [1, 0], 'D')

    return switch.to_instruction()
