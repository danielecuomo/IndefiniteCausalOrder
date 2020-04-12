#!/usr/bin/env python
# coding: utf-8

# In[3]:


from qiskit import QuantumCircuit, QuantumRegister

from qiskit.circuit import Parameter

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


theta0 = Parameter('$θ_0$')
phi0 = Parameter('$φ_0$')
lamb0 = Parameter('$λ_0$')

theta1 = Parameter('$θ_1$')
phi1 = Parameter('$φ_1$')
lamb1 = Parameter('$λ_1$')

theta2 = Parameter('$θ_2$')
phi2 = Parameter('$φ_2$')
lamb2 = Parameter('$λ_2$')


# In[7]:


q_switch = QuantumCircuit(2, name='q_switch')

#init qubits
q_switch.u3(theta0, phi0, lamb0, 0)
q_switch.h(1)

#reversed control-U
q_switch.x(1)
q_switch.cu3(theta1, phi1, lamb1, 1,0)
q_switch.x(1)

q_switch.barrier()

q_switch.u3(theta2, phi2, lamb2, 0)
q_switch.cu3(theta1, phi1, lamb1, 1,0)

#q_switch.draw(output='mpl', plot_barriers=False, initial_state=True)


# In[9]:


q_switch.draw(output="mpl", plot_barriers=False, initial_state=True).savefig("q_switch.svg", format="svg")


# In[ ]:




