#!/usr/bin/env python
# coding: utf-8

#Create a parametrized gate implementing a quantum switch.
#Input 0 is the target.
#Input 1 is an ancilla gate, therefore it will be reset to state |+>.

def getSwitchAsGate():
    theta1 = Parameter('$θ_1$')
    phi1 = Parameter('$φ_1$')
    lamb1 = Parameter('$λ_1$')

    theta2 = Parameter('$θ_2$')
    phi2 = Parameter('$φ_2$')
    lamb2 = Parameter('$λ_2$')

    q = QuantumRegister(1, name='q')
    a = QuantumRegister(1, name='a')
    switch = QuantumCircuit(q, a, name='$\mathcal{S}$')

    switch.reset(1)
    switch.h(1)
    switch.x(1)
    switch.cu3(theta1, phi1, lamb1, 1,0)
    switch.x(1)
    switch.barrier()
    switch.u3(theta2, phi2, lamb2, 0)
    switch.cu3(theta1, phi1, lamb1, 1,0)

    return switch.to_instruction()




